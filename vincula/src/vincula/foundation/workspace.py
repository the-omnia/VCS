"""Implementation of workspace entities."""

__all__ = [
	"Workspace",
]

from json import load as _json_load
from pathlib import Path as _Path
from typing import TYPE_CHECKING as __TYPE_CHECKING__

from .exceptions import WorkspaceNotFound as _WorkspaceNotFound
from .language import Language as _Language
from .module import Module as _Module

if __TYPE_CHECKING__:
	from typing import List
	from typing import Optional
	from pathlib import Path

	from .language import Language
	from .module import Module
	from .__workspace_typing__ import WorkspaceDeclaration


class Workspace:
	"""Main workspace controller.

	Workspace class controls loading/saving/caching of workspace entities: modules, languages, plugins etc.
	It is like core of runtime, but in case of control.

	Since:
	    0.1.0
	"""

	@property
	def bin_path(self) -> "Path":
		return self.__w_path__ / ".local" / "bin"

	@property
	def cache_path(self) -> "Path":
		return self.__w_path__ / ".local"

	@property
	def lib_path(self) -> "Path":
		return self.__w_path__ / ".local" / "lib"

	@property
	def plugin_path(self) -> "Path":
		return self.__w_path__ / ".local" / "plugins"

	@property
	def root(self) -> "Path":
		return self.__w_path__

	@property
	def languages(self) -> "List[Language]":
		return self.__languages__

	@property
	def modules(self) -> "List[Module]":
		return self.__modules__

	def create_build_box(self) -> None:
		pass

	def __init__(self, root: "Optional[str]" = None) -> None:
		"""Initiate workspace object.

		Construct workspace from groud up, loading all entities in workspace.

		Since:
		    0.1.0

		Throws:
		    * WorkspaceNotFound - In case if workspace not found.
		"""

		if root is None:
			root = _Path.cwd()  # type: ignore
		else:
			root = _Path(root)  # type: ignore

		self.__w_path__ = self.__find_root__(root)  # type: ignore

		try:
			self.__read_declaration__()

		except KeyError as key_error:
			raise key_error

		if not self.cache_path.exists():
			self.__init_cache__()

		self.__modules__: "List[Module]" = []

		self.__scan_modules_local__()

	def __init_cache__(self) -> None:
		"""Init cache system.

		Cache is more verbose elemnt of workspace. It contains installed elements, some specific declarations and
		runtime environments for commands and processes. In future it will come as abstraction over operating
		system.

		Since:
			0.1.0
		"""

		# General file system layout
		for entry in ["bin", "lib", "include", "cache", "plugins"]:
			with self.cache_path / entry as fs_entry:
				fs_entry.mkdir(parents=True)

	def __find_root__(self, root: "Path") -> "Path":
		"""Find root of workspace.

		Params:
		    * root - Path to current folder.

		Throws:
		    * WorkspaceNotFound - In case if workspace not found.

		Returns:
		    Absolute path to root folder
		"""

		if root.absolute() == "/":
			raise _WorkspaceNotFound("root workspace not found")

		for entry in root.iterdir():
			if entry.name == "workspace.json":
				return root

		return self.__find_root__(root.parent)

	def __read_declaration__(self) -> None:
		"""Read's main declaration and then loads it as elements.

		Since:
			0.1.0
		"""

		with (self.__w_path__ / "workspace.json").open() as wrk_file:
			decl: "WorkspaceDeclaration" = _json_load(wrk_file)

			# NOTE: For now this doesn't have any meaning, but in future, it will help to simplify
			#       trust process
			self.__org_id__ = decl["organization"]["id"]
			self.__org_name__ = decl["organization"]["name"]

			self.__repositories__ = []
			for repo_name in decl.get("repositories", {}).keys():  # type: ignore[override]
				pass

			self.__languages__: "List[Language]" = []
			for lang_name in decl.get("languages", {}).keys():  # type: ignore[override]
				language = _Language(
					decl["languages"][lang_name]["name"],  # type: ignore
					decl["languages"][lang_name]["version"],  # type: ignore
					lang_name,
				)

				self.__languages__.append(language)

	def __scan_modules_local__(self, root: "Optional[Path]" = None):
		"""Scan for modules in current workspace."""

		if root is None:
			root = self.__w_path__

		for entry in root.iterdir():
			if entry.name == "module.json":
				mod = _Module.from_file_path(entry, self.languages)
				self.__modules__.append(mod)

				return

			if entry.is_dir():
				self.__scan_modules_local__(entry)

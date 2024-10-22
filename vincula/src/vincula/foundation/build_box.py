"""Implementation of secured build-box.

Since:
	0.1.0

Copyright:
	Omnia Community, 2022 - current time

License:
	Omnia Closed Source License v1
"""

__all__ = [
	"BuildBox",
	"LinuxBuildBox",
	"MacOsBuildBox",
]

from abc import ABC as __ABC__
from abc import abstractmethod as _abstractmethod
from argparse import ArgumentError
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from json import dump as _json_dump
from json import load as _json_load
from uuid import uuid3 as _uuid3

from .module import Module as _Module
from .module import ModuleT as _ModuleT
from .lock import Locked as __Locked__

if __TYPE_CHECKING__:
	from typing import List
	from typing import Union
	from pathlib import Path
	from uuid import UUID

	from .module import ModuleT
	from .module import Module


class BuildBox(__ABC__):
	"""Abstraction layer over the files, execution and other elements of operating system.

	Class provides general interfaces for working with current environment as is. It copies required elements into
	runtime and then provides it as is. Don't use this class for running elements, rather, consider using native
	os implementation.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@property
	def path(self) -> "Path":
		return self.__b_path__

	@property
	def uuid(self) -> "UUID":
		return self.__b_uuid__

	def __create_build_box__(self) -> None:
		"""Create new build box file layout.

		Since:
			0.1.0
		"""

		for entry in ["bin", "lib", "include", "run", "etc", "mnt", "proc", "usr"]:
			entry_path = self.__b_path__ / entry
			entry_path.mkdir(exist_ok=True, parents=True)

		self.__b_environ__ = {
			"OS": "linux",
			"ARCH": "arch",
			"SHELL": "tunica",
			"PATH": "/bin:/usr/bin:/usr/local/bin",
		}
		with self.__b_path__ / "etc" / "build-box" / "environ" as environ_path:
			with environ_path.open(mode="w", encoding="utf-8") as environ_file:
				_json_dump(self.__b_environ__, environ_file)

	def __init__(
		self,
		desired_path: "Path",
		workspace_id: "UUID",
	) -> None:
		self.__b_modules__: "List[Module]" = []
		self.__b_uuid__ = _uuid3(
			workspace_id,
			desired_path.name,
		)
		self.__b_path__ = desired_path

		if not self.__b_path__.exists():
			self.__create_build_box__()
			return

	@_abstractmethod
	def __iadd__(self, element: "Module") -> None:
		raise NotImplementedError(
			"method '__iadd__' or '+=' operator is not implemented"
		)


class LinuxBuildBox(BuildBox):
	pass


class MacOsBuildBox(BuildBox):
	"""Implementation of MacOS build-box.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	def __init__(self, desired_path: "Path", workspace_id: "UUID") -> None:
		super().__init__(desired_path, workspace_id)

	def __iadd__(self, element: "Module") -> None:
		if element is None:
			raise ArgumentError("argument 'element' could not be None")

		if not isinstance(element, _Module):
			raise TypeError(
				"argument 'element' is not an instance of 'vincula.foundation.Module'"
			)

		# Support for executable type of modules.
		if element.type == _ModuleT.Executable:
			pass

		# Support for library type of modules.
		elif element.type == _ModuleT.Library:
			pass

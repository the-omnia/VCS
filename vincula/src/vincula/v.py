"""Implementation of root runtime controller.

Copyright:
	The Omnia community, 2022 - current time

License:
	Omnia Closed Source License v1
"""

from typing import TYPE_CHECKING as __TYPE_CHECKING__

from .buildin import CPythonPlugin
from .foundation import Workspace as _Workspace


if __TYPE_CHECKING__:
	from typing import List

	from .foundation import Module
	from .foundation import Workspace
	from .plugins import LanguagePlugin


class Vincula:
	"""Execution controller.

	Class provides general control over all workspaces on current and remote machines. Class is provided for
	future works, but in general, may work as single object to control different workspaces, executions etc.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@property
	def workspaces(self) -> "List[Workspace]":
		"""Getter for all workspaces.

		Wrapper around internal variable, which must be used instead of direct interractions with __v_workspaces_.

		Since:
			0.1.0
		"""

		return self.__v_workspaces__

	def create_build_box(self) -> None:
		pass

	def load_workspace(self, path: str) -> None:
		workspace = _Workspace(path)
		self.__v_workspaces__.append(workspace)

	def __init__(self) -> None:
		# TODO: Inject here loading of build-in plugins.
		self.__v_lang_plugins__: "List[LanguagePlugin]" = []

		self.__v_workspaces__: "List[Workspace]" = []

	def __init_subclass__(cls) -> None:
		raise PermissionError("Class 'Vincula' could should not be override")

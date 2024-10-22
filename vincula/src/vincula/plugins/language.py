__all__ = [
	"LanguagePlugin",
]


from abc import ABC as __ABC__
from abc import abstractmethod as __abstract__
from typing import TYPE_CHECKING as __TYPE_CHECKING__

from vincula.foundation.lock import Locked as __Locked__

from .__foundation__ import BasePlugin as __BasePlugin__

if __TYPE_CHECKING__:
	from typing import List
	from pathlib import Path

	from vincula.foundation import Module

	from .repository import Repository


class LanguagePlugin(__BasePlugin__, __Locked__, __ABC__):
	"""Base language plugin.

	This type of plugins allows end developer to add special support for any programming language.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@__abstract__
	def execute(self, module: "Module", command: str) -> None:
		"""Execute module command using internal capabilities.

		Method must execute command in runtime of module in special sandbox. Arguments passed inside this method
		must follow convention of name of possible execution.

		Params:
			* module - Module on which command is executed.
			* command - String representation on which command is executed.

		Since:
			0.1.0
		"""

	@__abstract__
	def migrate(self, module: "Module"):
		"""Migrate module from it's native format into one, general vincula format."""

		raise NotImplementedError("method 'migrate' is not implemented")

	@__abstract__
	def scan(self, path: "Path") -> "List[Module]":
		"""Scan all repository on possible formats of modules according to language tooling and specs."""

		raise NotImplementedError("method 'scan' is not implemented")

	def __init__(self, cache_path: "Path") -> None:
		super().__init__(cache_path)

__all__ = [
	"Dependency",
]

from abc import ABC as __ABC__
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__

from vincula.foundation.lock import Locked as __Locked__


if __TYPE_CHECKING__:
	from typing import List
	from pathlib import Path


class Dependency(__Locked__, __ABC__):
	"""General dependency representation.

	Version:
		0.1.0

	Since:
		0.1.0
	"""

	@staticmethod
	@_abstractmethod
	def from_definition(uri: str) -> "Dependency":
		raise NotImplementedError("static method 'from_definition' is not implemented")

	@_abstractmethod
	def install(self) -> None:
		raise NotImplementedError("static method 'install' is not implemented")

	@property
	@_abstractmethod
	def dependency(self) -> "List[str]":
		raise NotImplementedError("property 'dependencies' is not implemented")

	@_abstractmethod
	def __init__(self, location: "Path") -> None:
		super().__init__()

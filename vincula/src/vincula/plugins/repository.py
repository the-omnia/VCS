__all__ = [
	"Repository",
]

from abc import ABC as __ABC__
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__

if __TYPE_CHECKING__:
	from typing import Literal
	from typing import List
	from typing import Union

	from .dependency import Dependency


class Repository(__ABC__):
	"""Repository base representation.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@_abstractmethod
	def install(
		self, name: str, version: "Union[str, Literal['latest']]"
	) -> "Dependency":
		raise NotImplementedError("method 'install' not implemented")

	@_abstractmethod
	def search(self, name: str) -> "List[Dependency]":
		raise

	def __init__(self, name: str, url: str) -> None:
		super().__init__()

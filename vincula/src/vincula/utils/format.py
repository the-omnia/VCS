__all__ = [
	"Format",
]

from typing import TYPE_CHECKING as __TYPE_CHECKING__
from inspect import currentframe as _frames

if __TYPE_CHECKING__:
	from typing import List

	from .__format_typing__ import Insertion


class Format:
	"""General formatting element.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	def insert(self, **kwargs: "Insertion") -> bytes:
		result: bytes = bytes()

		for key in kwargs.keys():
			result.join(f"{kwargs[key]} ".encode())

		return result

	def __init__(self, format: str) -> None:
		self.__f_name__: "List[str]" = []
		self.__f_type__: "List[str]" = []

		self.__parse__(format)

	def __parse__(self, format: str) -> None:
		elements = format.split(" ")
		for element in elements:
			element = element.strip(" ")
			try:
				name, type = element.split(":")
				if type not in ["str", "int", "float"]:
					raise TypeError()

				self.__f_name__.append(name)
				self.__f_type__.append(type)

			except ValueError:
				...

			except:
				...

	def __str__(self) -> str:
		return ""

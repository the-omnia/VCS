"""Implementation of lock file entity.

Copyright:
	The Omnia Community 2022 - current time.

License:
	Omnia Closed Source License v1
"""

__all__ = [
	"Locked",
	"LockFile",
	"LockEntity",
]

from abc import ABC as __ABC__
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from enum import Enum as __Enum__

from .exceptions import LockFileNotFound as _LockFileNotFound
from .exceptions import LockFileMalformed as _LockFileMalformed

if __TYPE_CHECKING__:
	from typing import Type
	from typing import List
	from io import BufferedReader
	from pathlib import Path


class Locked(__ABC__):
	"""Abstract class for any lockable entity.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@staticmethod
	@_abstractmethod
	def load(decl: bytes) -> "Locked":
		raise NotImplementedError("method 'load' is not implemented")

	@_abstractmethod
	def lock(self) -> bytes:
		"""Lock object for further faster loading.

		Since:
			0.1.0
		"""

		raise NotImplementedError("method 'lock' is not implemented")


class LockEntity(__Enum__):
	Module = 0x1


class LockFile:
	"""Lock object which contains compressed elements of workspace.

	LockFile used for fast loading of workspace. If something is missing it would
	not do anything to prevent such things. Instead lock files are used for loading
	elements into workspace.

	Since:
		0.1.0

	Version:
		0.1.0

	Authors:
		* Mark Sorokin
	"""

	@property
	def empty(self) -> bool:
		return self.__l_empty__

	def get(self, example: "Type[Locked]") -> "List[Locked]":
		"""Get list of entities by class type.

		Params:
			* example - Class, which will be used as template.

		Since:
			0.1.0
		"""

		elements: "List[example]" = []
		for el in self.__l_elements__:
			if el.__class__ == example:
				elements.append(el)

		return elements

	def write(self) -> None:
		with self.__l_path__.open("wb") as lock_file:
			# Writting header
			lock_file.write(b"VLF\n")

			# Writting elements
			for el in self.__l_elements__:
				lock_file.write(el.lock() + b"\n")

	def __init__(self, lock_file_path: "Path") -> None:
		"""Initiate lock file object.

		Params:
			* lock_file_path - Path object, which points to lock file, not directory.

		Raises:
			* LockFileNotFound - Error thrown when file does not exists.
		"""

		if not lock_file_path.exists():
			raise _LockFileNotFound("file is missing", lock_file_path)

		self.__l_path__ = lock_file_path
		self.__l_elements__: "List[Locked]" = []

		try:
			with lock_file_path.open("rb") as lock_file:
				self.__read_header__(lock_file)

			self.__l_empty__ = False

		except _LockFileMalformed:
			self.__l_empty__ = True

	def __read_header__(self, file: "BufferedReader") -> None:
		line = file.readline()

		if line[0:2] != "VLF":
			raise _LockFileMalformed(
				"header is missing", self.__l_path__, 0, 0, 2, line[0:2].decode(), "VLF"
			)

	def __iadd__(self, el: Locked) -> None:
		if not issubclass(el.__class__, Locked):
			raise TypeError("rvalue is not subclass of element")

"""Collection of exceptions used across foundation package.

Copyright:
	The Omnia Community, 2022 - current time

License:
	Omnia Closed Source License v1
"""

__all__ = [
	# Lock related errors
	"LockFileError",
	"LockFileNotFound",
	"LockFileMalformed",
	# General wrapper for error
	"VinculaError",
]

from abc import ABC as __ABC__
from typing import TYPE_CHECKING as __TYPE_CHECKING__

if __TYPE_CHECKING__:
	from typing import Callable
	from typing import Optional
	from pathlib import Path


class VinculaError(__ABC__, BaseException):
	@property
	def deffer(self) -> "Callable[[], ]":
		return self.__e_deffer__

	@property
	def message(self) -> str:
		return self.__e_msg__

	def __init__(self, message: str, deffer: "Optional[Callable[[],]]" = None) -> None:
		self.__e_msg__ = message
		if deffer:
			self.__e_deffer__ = deffer
		else:
			self.__e_deffer__ = lambda: None


class LockFileError(VinculaError):
	"""General lock file error.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@property
	def path(self) -> "Path":
		return self.__e_path__

	def __init__(
		self,
		message: str,
		path: "Path",
		deffer: "Optional[Callable[[],]]" = None,
	) -> None:
		super().__init__(message, deffer)

		self.__e_path__ = path


class LockFileNotFound(LockFileError):
	"""Error thrown when lock file not provided.

	Error-marker, which is thrown when provided path for lock file does not really exists. Used internally in workspace
	for better logic separation. In cases, when this error must be thrown in user space consider avoiding it, due to this
	is mostly internal error, not users.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	def __init__(
		self,
		message: str,
		path: "Path",
		deffer: "Optional[Callable[[],]]" = None,
	) -> None:
		super().__init__(message, path, deffer)


class LockFileMalformed(LockFileError):
	"""General error thrown when lock-file is malformed.

	Error thrown when lock-file is malformed in different places. Could be used for indicating of general, critical errors,
	or in places, where some plugin generates bad byte orders.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@property
	def line(self) -> int:
		return self.__e_line__

	@property
	def start(self) -> int:
		return self.__e_start__

	@property
	def end(self) -> int:
		return self.__e_end__

	@property
	def provided(self) -> str:
		return self.__e_provided__

	@property
	def should(self) -> str:
		return self.__e_should__

	def __init__(
		self,
		message: str,
		path: "Path",
		line: int,
		start: int,
		end: int,
		provided: str,
		should: str,
		deffer: "Optional[Callable[[],]]" = None,
	) -> None:
		super().__init__(message, path, deffer)

		self.__e_line__ = line
		self.__e_start__ = start
		self.__e_end__ = end
		self.__e_provided__ = provided
		self.__e_should__ = should


class WorkspaceError(VinculaError):
	pass


class WorkspaceNotFound(WorkspaceError):
	pass

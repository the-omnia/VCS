__all__ = [
	"Library",
]

from typing import TYPE_CHECKING as __TYPE_CHECKING__

if __TYPE_CHECKING__:
	from pathlib import Path


class Library:
	def __init__(
		self, name: str, version: str, path: "Path", install_path: "Path"
	) -> None:
		self.__l_name__ = name
		self.__l_version__ = version
		self.__l_path__ = path
		self.__l_install__ = install_path

		self.__scan_files__()

	def __scan_files__(self) -> None:
		"""Scan library files for required entities."""

		for entity in self.__l_path__.iterdir():
			pass

from typing import TYPE_CHECKING as __TYPE_CHECKING__
from pathlib import Path as __Path
from json import load as __json_load

if __TYPE_CHECKING__:
	from typing import Union
	from pathlib import Path

	from .__package_typing__ import PackageDeclaration
	from .library import Library


class VpfPackage:
	def __init__(self, path: "Union[str, Path]") -> None:
		global __Path

		if isinstance(path, __Path):
			self.__p_path__ = path
		elif isinstance(path, str):
			self.__p_path__ = __Path(path)
		else:
			# NOTE(assertionbit): Provided for those, who don't use type-checker
			raise TypeError("argument 'path' not type of 'str' or 'pathlib.Path'")

		if not self.__p_path__.exists():
			raise FileExistsError("package file doesn't exists", f"{self.__p_path__}")

		if self.__p_path__.name == "vpf.json":
			self.__load_raw_declaration__()
			return

	def __load_declaration__(self) -> None:
		pass

	def __load_raw_declaration__(self) -> None:
		global __json_load

		with self.__p_path__.open("r") as decl_file:
			decl: "PackageDeclaration" = __json_load(decl_file)

			self.__p_name__ = decl["name"]
			self.__p_version__ = decl["version"]

	def __lt__(self, pkg: "VpfPackage") -> bool:
		return False

	def __load_file__(self) -> None:
		pass

"""Implementation of module entities.

Since:
	0.1.0

Copyright:
	The Omnia Community, 2022 - current time

License:
	Omnia Closed Source License v1
"""

__all__ = [
	"Module",
	"ModuleT",
	"ModuleLayout",
]

from typing import TYPE_CHECKING as __TYPE_CHECKING__
from enum import Enum as __Enum__
from json import dump as _json_dump
from json import load as _json_load
from struct import Struct as __Struct

from .lock import Locked as __Locked__

if __TYPE_CHECKING__:
	from typing import List
	from pathlib import Path

	from .__module_typing__ import ModuleDecl
	from .__module_typing__ import ModuleDependenciesT
	from .language import Language


class ModuleT(__Enum__):
	Executable = "executable"
	Library = "library"


class ModuleLayout(__Enum__):
	SrcBased = "'src' based"
	Flat = "flat"


class Module(__Locked__):
	"""Module object implementation.

	Since:
	    0.1.0

	Version:
	    0.1.0
	"""

	@staticmethod
	def from_file_path(path: "Path", languages: "List[Language]") -> "Module":
		"""Load module from given file path.

		Method will analyze current workspace module and load it, with all elements. It will check type,
		layout and other aspects of module, with neccesery elements in it.

		Params:
			* path - pathlib.Path, object pointing to 'module.json' file.
			* languages - List[Language], collection of known languages.

		Returns:
			Loaded module with all elements in it.

		Since:
			0.1.0
		"""

		with path.open() as decl_file:
			decl: "ModuleDecl" = _json_load(decl_file)

			name = decl["general"]["name"]
			version = decl["general"]["version"]
			language = decl["general"]["language"]

			lang = None

			for l in languages:
				if l.name == language:
					lang = l

			if lang is None:
				raise

			dependencies = decl["dependencies"]

			layout: ModuleLayout = ModuleLayout.Flat
			if (path.parent / ("src")).exists():
				layout = ModuleLayout.SrcBased

			m_type: ModuleT = ModuleT.Library
			if layout == ModuleLayout.SrcBased:
				src_path = path.parent
				print(src_path / name)
				if (src_path / "main.py").exists() or (
					src_path / f"{name}.py"
				).exists():
					m_type = ModuleT.Executable

				src_path = src_path / "src"

				if (src_path / name / "main.py").exists() or (
					src_path / name / "__main__.py"
				).exists():
					m_type = ModuleT.Executable

			print(path)

			return Module(
				name,
				version,
				lang,
				dependencies,
				path.parent,
				m_type,
				layout,
			)

	@staticmethod
	def load(data: bytes) -> "Module":
		"""Load module from lock file state."""

	def lock(self) -> bytes:
		data = bytes()

		return data

	@property
	def name(self) -> str:
		return self.__m_name__

	@property
	def path(self) -> "Path":
		return self.__m_path__

	@property
	def language(self) -> "Language":
		return self.__m_lang__

	@property
	def type(self) -> ModuleT:
		return self.__m_type__

	@property
	def layout(self) -> ModuleLayout:
		return self.__m_layt__

	def __init__(
		self,
		name: str,
		version: str,
		language: "Language",
		dependencies: "ModuleDependenciesT",
		path: "Path",
		type: ModuleT,
		layout: ModuleLayout,
	) -> None:
		self.__m_name__ = name
		self.__m_vers__ = version
		self.__m_lang__ = language
		self.__m_path__ = path
		self.__m_type__ = type
		self.__m_layt__ = layout
		self.__m_deps__ = dependencies

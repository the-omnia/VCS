from typing import TYPE_CHECKING as __TYPE_CHECKING__

from vincula.plugins import LanguagePlugin as __LanguagePlugin__

if __TYPE_CHECKING__:
	from typing import List
	from pathlib import Path

	from vincula.foundation import Module
	from vincula.plugins.__foundation_typing__ import PluginInfo


class CPythonPlugin(__LanguagePlugin__):
	"""Fallback python plugin.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@staticmethod
	def load(decl: bytes) -> "CPythonPlugin":
		"""Load plugin from from lock file.

		Since:
			0.1.0
		"""
		pass

	def info(self) -> "PluginInfo":
		return {
			"name": "cpython",
			"version": "0.1.0",
			"languages": {
				"cpython": {
					"provides-range": ["3.7"],
					"default-edition": "cpython",
					"default-version": "3.7",
					"file-extensions": ["py", ".pyi"],
					"project-markers": [
						"pyproject.toml",
						"Pipfile",
						"Pipfile.lock",
						"requirements.txt",
					],
					"provided-edition": ["cpython"],
				}
			},
		}

	def scan(self, path: "Path") -> "List[Module]":
		return super().scan(path)

	def execute(self, module: "Module", command: str) -> None: ...

	def lock(self) -> None:
		return

	def migrate(self, module: "Module"): ...

	def __init__(self, cache_path: "Path") -> None:
		super().__init__(cache_path)
		self.__init_cache__()

	def __init_cache__(self) -> None:
		pass

	def __load_sdks__(self) -> None:
		pass

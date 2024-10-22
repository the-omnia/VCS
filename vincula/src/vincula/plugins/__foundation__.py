__all__ = [
	"BasePlugin",
	"PluginLoader",
]

from abc import ABC as __ABC__
from abc import abstractmethod as _abstractmethod
from typing import TYPE_CHECKING as __TYPE_CHECKING__

if __TYPE_CHECKING__:
	from pathlib import Path

	from .__foundation_typing__ import PluginInfo


class BasePlugin(__ABC__):
	"""Base type for all type of plugins.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@_abstractmethod
	def info(self) -> "PluginInfo":
		"""Return information about current state of plugin.

		Returns:
			Dictionary, which must contain structured information about plugin.

		Since:
			0.1.0
		"""

		raise NotImplementedError("method 'info' is not implemented")

	@property
	def cache_path(self) -> "Path":
		"""Get cache path of plugin."""
		return self.__p_cache_path__

	def __init__(self, cache_path: "Path") -> None:
		self.__p_cache_path__ = cache_path


class PluginLoader:
	def load(self, path: "Path") -> BasePlugin:
		return BasePlugin(path)  # type: ignore

	def __init__(self) -> None:
		pass

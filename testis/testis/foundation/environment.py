__all__ = [
	"Environment",
]


from os import environ as _environ
from typing import TYPE_CHECKING as __TYPE_CHECKING__

if __TYPE_CHECKING__:
	from pathlib import Path


class Environment:
	"""Environment of single execution process.

	When testis executes steps, groups or other elemens of runtime, it provides special environment for
	runtime. It controls: environment variables, folders, access etc.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	@property
	def env(self):
		pass

	def __init__(self, runtime_folder: "Path", logging_folder: "Path") -> None:
		self.__runtime_folder__ = runtime_folder
		self.__logging_folder__ = logging_folder

from typing import TYPE_CHECKING as __TYPE_CHECKING__
from pathlib import Path as __Path

from vincula.plugins import Repository as __Repository

if __TYPE_CHECKING__:
	from typing import Literal
	from typing import List
	from typing import Union

	from vincula.plugins import Dependency


class LocalRepository(__Repository):
	"""Implementation of local repository.

	Local repository is implementation of storage object in root of workspace.

	Since:
		0.1.0
	"""

	def search(self, name: str) -> "List[Dependency]":
		"""Search for all possible elements to install.

		Params:
			* name - String, containing name of package to install.

		Since:
			0.1.0
		"""

		results: "List[Dependency]" = []

		return results

	def install(
		self, name: str, version: "Union[str, Literal['latest']]"
	) -> "Dependency":
		raise TypeError()

	def __init__(self, name: str, url: str) -> None:
		global __Path

		self.__r_path__ = __Path(url)
		self.__init_cache__()

	def __init_cache__(self) -> None:
		pass

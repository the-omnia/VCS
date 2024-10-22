from typing import TYPE_CHECKING as __TYPE_CHECKING__
from os import fork as __fork
from pathlib import Path as __Path
from sqlite3 import connect as __connect
from subprocess import Popen as __Popen
from signal import signal as __signal_handle

from .app import Application as __App

if __TYPE_CHECKING__:
	from typing import List
	from typing import Union
	from pathlib import Path

	from .app import Application


STORAGE_JOIN = 120
"""Signal join"""


class Storage:
	"""Storage - place where all elements will be installed."""

	@property
	def applications(self) -> "List[Application]":
		selections = self.__lock_db__.execute("SELECT * FROM applications").fetchall()

		apps: "List[Application]" = []

		for selection in selections:
			app_name = f"{selection[0]}.app"

			app = __App(
				selection[0],
				selection[1],
				self.__store_path__ / app_name / "Executables",
				self.__store_path__ / app_name / "Resources",
				self.__store_path__ / app_name / "Logs",
				True,
			)

			apps.append(app)

		return apps

	def demonize(self) -> None:
		"""Start storage process as demon.

		Since:
			0.1.0
		"""

		pid = __fork()
		if pid == 0:
			return

		with open(f"/proc/storage-{123}", "w") as pid_file:
			pid_file.write(f"{pid}")

		__signal_handle(STORAGE_JOIN, self.__handle_join__)

	def __init__(self, location: "Union[str, Path]") -> None:
		global __Path

		if isinstance(location, str):
			self.__store_path__ = __Path(location)
		elif isinstance(location, __Path):
			self.__store_path__ = location
		else:
			raise TypeError("argument 'location' not of type 'str' or 'pathlib.Path'")

		if not self.__store_path__.exists():
			self.__init_storage__()

		else:
			self.__load_lock_db__()

	def __init_storage__(self) -> None:
		self.__lock_db__ = __connect(self.__store_path__ / "lock.db")

		self.__lock_db__.execute("""CREATE TABLE IF NOT EXISTS applications (
			name VARCHAR(128),
			version VARCHAR(128),
		);""")

	def __load_lock_db__(self) -> None:
		global __connect

		self.__lock_db__ = __connect(self.__store_path__ / "lock.db")

	def __handle_join__(self, _, __) -> None:
		pass

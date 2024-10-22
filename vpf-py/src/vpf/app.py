__all__ = [
	"Application",
]

from os import X_OK as _OS_X_OK
from os import access as _os_access
from os import environ as _environ
from typing import TYPE_CHECKING as __TYPE_CHECKING__
from pathlib import Path as __Path
from subprocess import Popen as _Popen

from .exceptions import VpfError as __VpfError__

if __TYPE_CHECKING__:
	from pathlib import Path


class ApplicationError(__VpfError__):
	def __init__(self, name: str, *args: object) -> None:
		super().__init__(*args)
		self.__app_name__ = name


class LayoutError(ApplicationError):
	def __init__(self, name: str, location: str, *args: object) -> None:
		super().__init__(name, *args)
		self.__app_location__ = location


class ResourceMalformed(ApplicationError):
	def __init__(self, name: str, resource_name: str, *args: object) -> None:
		super().__init__(name, *args)
		self.__app_resource__ = resource_name


class ExecutableMalformed(ApplicationError):
	def __init__(self, name: str, executable_path: str, *args: object) -> None:
		super().__init__(name, *args)
		self.__app_executable__ = executable_path


class Application:
	@property
	def name(self) -> str:
		return self.__app_name__

	@property
	def version(self) -> str:
		return self.__app_version__

	@property
	def is_installed(self) -> bool:
		return self.__app_installed__

	def check(self) -> None:
		"""Check if application state is normal.

		Method will check file-system layout and check if resources, declarations, elements and other runtime
		elements are valid. Check is depending on OS, so for testing purpose, consider using non-installed version
		of application or use installed version on different operating systems.

		Raise:
			* LayoutError - In case when application layout is malformed.
			* ExecutableMalformed - In case when executable file is not a file, executable or not appears in fs.

		Since:
			0.1.0
		"""
		global _OS_X_OK
		global _os_access

		for path in [self.__app_rescs__, self.__app_logging__, self.__app_src__]:
			if not path.exists():
				raise LayoutError(self.__app_name__, f"{path}")

		with self.__app_src__ / "app" as exe:
			if not exe.exists():
				raise ExecutableMalformed(self.__app_name__, f"{exe}")

			if exe.is_dir():
				raise ExecutableMalformed(self.__app_name__, f"{exe}")

			if not _os_access(exe, _OS_X_OK):
				raise ExecutableMalformed(self.__app_name__, f"{exe}")

		if not self.is_installed:
			return

	def run(self) -> int:
		"""Run application.

		Since:
			0.1.0
		"""

		env = _environ.copy()
		env["APP_RESOURCES"] = f"{self.__app_src__}"
		env["APP_LOGGING"] = f"{self.__app_logging__}"

		process = _Popen(
			[],
			executable=self.__app_src__ / "app",
			env=env,
		)

		result = process.wait()
		if result == 0:
			return 0

		process.communicate()

		return 1

	def update(self, updated_to: "Application") -> None:
		"""Update current application to more modern state.

		Params:
			* updated_to - Pointer to not-unpacked another, new version of package.

		Since:
			0.1.0

		Version:
			0.1.0
		"""

		pass

	def __init__(
		self,
		name: str,
		version: str,
		src_location: "Path",
		resource_location: "Path",
		logging_location: "Path",
		is_installed: bool,
	) -> None:
		self.__app_name__ = name
		self.__app_version__ = version
		self.__app_src__ = src_location
		self.__app_rescs__ = resource_location
		self.__app_logging__ = logging_location
		self.__app_installed__ = is_installed

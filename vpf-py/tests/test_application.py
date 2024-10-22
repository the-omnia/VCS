from pathlib import Path
from unittest import TestCase

from src.vpf.app import Application, LayoutError, ResourceMalformed


class TestApplicationObject(TestCase):
	def fixture(self) -> Application:
		return Application(
			"Example",
			"0.1.0",
			Path("..") / "fixtures" / "vpf" / "example.app" / "Executables",
			Path("..") / "fixtures" / "vpf" / "example.app" / "Resources",
			Path("..") / "fixtures" / "vpf" / "example.app" / "Logs",
			False,
		)

	def test_init_fixture(self) -> None:
		app = self.fixture()

	def test_application_verify(self) -> None:
		app = self.fixture()

		try:
			app.check()

		except ResourceMalformed as e:
			self.assertFalse(
				True,
				f"application thrown error on checks: resource malformed ({e.__app_resource__})",
			)

		except LayoutError as e:
			self.assertFalse(
				True,
				f"application thrown error on checks: layout is malformed: ({e.__app_location__})",
			)

	def test_application_execute(self) -> None:
		app = self.fixture()

		self.assertEqual(0, app.run())

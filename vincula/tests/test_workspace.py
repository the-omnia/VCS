from unittest import TestCase

from vincula.foundation import Workspace


class TestWorkspace(TestCase):
	def test_workspace_init(self) -> None:
		workspace = Workspace()

		self.assertEqual(
			1, len(workspace.languages), "number of loaded languages is incorrect"
		)
		self.assertEqual(
			2, len(workspace.modules), "number of loaded modules is incorrect"
		)

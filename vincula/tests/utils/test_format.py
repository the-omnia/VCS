from unittest import TestCase

from src.vincula.utils import Format


class TestFormat(TestCase):
	def testBasicFormat(self):
		f = Format("")
		f.insert(hello="world")

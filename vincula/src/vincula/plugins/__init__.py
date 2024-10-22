"""Plugins API for extending existing functionality."""

__all__ = [
	"Dependency",
	"LanguagePlugin",
	"Repository",
]


from .dependency import Dependency
from .language import LanguagePlugin
from .repository import Repository

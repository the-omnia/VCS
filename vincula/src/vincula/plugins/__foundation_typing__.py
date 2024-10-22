__all__ = [
	"PluginInfo",
]


from typing import Dict as __Dict__
from typing import List as __List__
from typing import Optional as __Optional__
from typing import TypedDict as __TypedDict__


LanguageCapabilities = __TypedDict__(
	"LanguageCapabilities",
	{
		"provides-range": __List__[str],
		"default-edition": str,
		"default-version": str,
		"file-extensions": __List__[str],
		"project-markers": __List__[str],
		"provided-edition": __Optional__[__List__[str]],
	},
)
"""Declaration of language capabilities through plugin.

Example:
	>>> {
	... 	# ...
	... 	"python": {
	... 		"provides-range": ["3.0", "3.13"],
	... 		"default-edition": "cpython",
	... 		"default-version": "3.13",
	... 		"file-extensions": ["py", "pyi"],
	... 		"project-markers": ["pyproject.toml", "setup.py"]
	... 	}
	... }

Since:
	0.1.0

Version:
	0.1.0
"""

PluginInfo = __TypedDict__(
	"PluginInfo",
	{
		"name": str,
		"version": str,
		"languages": __Optional__[__Dict__[str, LanguageCapabilities]],
	},
)

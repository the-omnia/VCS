__all__ = ["PackageDeclaration"]

from typing import Dict as __Dict
from typing import TypedDict as __TypedDict


PackageDeclaration = __TypedDict(
	"PackageDeclaration",
	{
		"name": str,
		"version": str,
		"links": __Dict[str, str],
	},
)

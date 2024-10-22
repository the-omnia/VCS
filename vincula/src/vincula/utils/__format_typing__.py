__all__ = [
	"Convertable",
	"Insertion",
]


from typing import Dict as __Dict__
from typing import TypeVar as __TypeVar__


Convertable = __TypeVar__("Convertable", int, str, float)

Insertion = __Dict__[str, Convertable]

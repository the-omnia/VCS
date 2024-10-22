__all__ = [
	"ByteStruct",
]

from typing import TYPE_CHECKING as __TYPE_CHECKING__
from typing import Generic as __Generic__
from typing import TypeVar as __TypeVar__
from typing import Sized as __Sized__

if __TYPE_CHECKING__:
	from typing import Union


T = __TypeVar__("T")


class ByteStruct(__Sized__, __Generic__[T]):
	"""Alternative way of working with byte data.

	Since:
		0.1.0

	Version:
		0.1.0
	"""

	def __init__(self, format) -> None:
		pass

	def __len__(self) -> int:
		return 0

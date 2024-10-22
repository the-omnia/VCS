"""Typing annotations for language entity."""

__all__ = [
    "LanguageEntity",
]

from typing import TypedDict as __TypedDict__
from typing import Optional as __Optional__


LanguageEntity = __TypedDict__(
    "LanguageEntity",
    {
        "name": str,
        "version": str,
        "repository": __Optional__[str],
    },
)

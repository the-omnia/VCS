"""Type helpers for workspace module."""

__all__ = []


from typing import Dict as __Dict__
from typing import TypedDict as __TypedDict__
from typing import Optional as __Optional__

from .__language_typing__ import LanguageEntity as __LanguageEntity__


RepositoryDecl = __TypedDict__(
    "RepositoryDecl",
    {
        "type": str,
        "url": str,
    },
)
""""""


OrganizationDecl = __TypedDict__(
    "OrganizationDecl",
    {
        "id": str,
        "name": str,
    },
)
"""Declaration of organization."""

WorkspaceDeclaration = __TypedDict__(
    "WorkspaceDeclaration",
    {
        "organization": OrganizationDecl,
        "repositories": __Optional__[__Dict__[str, RepositoryDecl]],
        "languages": __Optional__[__Dict__[str, __LanguageEntity__]],
    },
)

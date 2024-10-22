"""Typing annotations for vincula.foundation.module."""

__all__ = [
	"DependencyDecl",
	"GeneralDecl",
	"ModuleDecl",
]

from typing import List as __List__
from typing import Dict as __Dict__
from typing import TypedDict as __TypedDict__
from typing import TypeVar as __TypeVar__
from typing import Literal as __Literal__
from typing import Optional as __Optional__
from typing import Union as __Union__


GeneralDecl = __TypedDict__(
	"GeneralDecl",
	{
		"name": str,
		"language": str,
		"version": str,
	},
)


DependencyDecl = __TypedDict__(
	"DependencyDecl",
	{
		"name": str,
		"version": str,
		"repository": __Optional__[str],
	},
)


DefaultDependencies = __Literal__["default"]
DeveloperDependencies = __Literal__["development"]


ModuleDependenciesT = __TypeVar__(
	"ModuleDependenciesT",
	__Dict__[
		__Union__[DefaultDependencies, DeveloperDependencies, str],
		__List__[DependencyDecl],
	],
	dict,
)


ModuleDecl = __TypedDict__(
	"ModuleDecl",
	{
		"general": GeneralDecl,
		"dependencies": ModuleDependenciesT,
	},
)

"""Implementation of language entitiy."""

__all__ = [
    "Language",
]


class Language:
    @property
    def name(self) -> str:
        return self.__l_name__

    @property
    def version(self) -> str:
        return self.__l_vers__

    @property
    def used_name(self) -> str:
        return self.__l_usnm__

    def __init__(
        self,
        name: str,
        version: str,
        used_name: str,
    ) -> None:
        self.__l_name__ = name
        self.__l_vers__ = version
        self.__l_usnm__ = used_name

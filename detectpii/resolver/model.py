import abc

from attr import define


@define(kw_only=True, frozen=True)
class Resolver:
    """Resolves credentials."""

    name: str

    @abc.abstractmethod
    def resolve(self, credential: str):
        raise NotImplementedError()

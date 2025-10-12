import abc

from attr import define


@define(kw_only=True, frozen=True)
class Resolver(abc.ABC):
    """Resolves credentials."""

    name: str

    @abc.abstractmethod
    def resolve(self, credential: str):
        raise NotImplementedError()

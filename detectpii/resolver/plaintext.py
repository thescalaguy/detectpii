from typing import Any

from attr import define

from detectpii.resolver.model import Resolver


@define(kw_only=True)
class PlaintextResolver(Resolver):
    """Resolves credentials provided in plaintext."""

    name: str = "PlaintextResolver"

    def resolve(self, credential: Any) -> Any:
        return credential


@define(kw_only=True)
class NoneResolver(Resolver):
    """Placeholder resolver for creating a tagged union."""

    name: str = "NoneResolver"

    def resolve(self, credential: Any) -> Any:
        return None

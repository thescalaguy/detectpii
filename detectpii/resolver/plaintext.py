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
class DummyResolver(Resolver):
    """Resolves credentials provided in plaintext."""

    name: str = "PlaintextResolver"

    def resolve(self, credential: Any) -> Any:
        return None

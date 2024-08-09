import os
from typing import Any

from attr import define

from detectpii.resolver.model import Resolver


@define(kw_only=True)
class EnvironmentResolver(Resolver):
    """Resolves credentials from environment variables"""

    name: str = "EnvironmentResolver"

    def resolve(self, credential: Any) -> Any:
        return os.environ.get(credential)

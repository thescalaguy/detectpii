from typing import Iterator

from attr import define

from detectpii.model import Catalog, Table


@define(kw_only=True)
class EmptyCatalog(Catalog):
    def detect_tables(self) -> None:
        pass

    def sample(self, table: Table, *args, **kwargs) -> Iterator[dict]:
        pass


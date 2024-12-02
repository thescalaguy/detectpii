from typing import Sequence

from sqlalchemy import Engine, create_engine

from detectpii.model import Catalog, Table, Column


class TestCatalog(Catalog):
    """A catalog to be used only for testing."""

    def engine(self) -> Engine:
        return create_engine("sqlite://")

    def detect_tables(self) -> None:
        table = Table(
            name="person",
            schema="public",
            columns=[
                Column(name="name"),
                Column(name="address"),
                Column(name="favorite_color"),
            ],
        )

        self.tables.append(table)

    def sample(self, table: Table, *args, **kwargs) -> Sequence[dict]:
        return [
            {
                "name": "John",
                "address": "123 Apple Street",
                "favorite_color": "blue",
            }
        ]

from typing import Sequence

from attr import define
from sqlalchemy import Engine, create_engine, text, Connection, Row
from trino.sqlalchemy import URL

from detectpii.model import Catalog, Column, Table


@define(kw_only=True)
class TrinoCatalog(Catalog):
    """A collection of tables in a Trino catalog and schema."""

    user: str
    password: str
    host: str
    port: int
    catalog: str
    schema: str

    def engine(self) -> Engine:
        return create_engine(self.url)

    def detect_tables(self) -> None:
        trino_engine = self.engine()

        with trino_engine.connect() as conn:

            for row in self._table_names(conn=conn):
                (table_name,) = row

                self._add_table_to_catalog(
                    table_name=table_name,
                    conn=conn,
                )

    @property
    def url(self) -> URL:
        return URL(
            host=self.host,
            user=self.user,
            port=self.port,
            password=self.password,
            catalog=self.catalog,
            schema=self.schema,
        )

    def _table_names(self, conn: Connection) -> Sequence[Row]:
        query = text("SHOW TABLES")
        return conn.execute(statement=query).fetchall()

    def _add_table_to_catalog(self, table_name: str, conn: Connection) -> None:
        query = text(f"DESCRIBE {table_name}")

        columns = [
            Column(name=column[0])
            for column in conn.execute(statement=query).fetchall()
        ]

        table = Table(
            name=table_name,
            schema=self.schema,
            columns=columns,
        )

        self.tables.append(table)

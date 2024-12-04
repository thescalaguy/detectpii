from functools import cached_property
from typing import Sequence

from attr import define
from sqlalchemy import Engine, create_engine, text, Connection, Row, MappingResult
from trino.sqlalchemy import URL

from detectpii.model import Column, Table, SQLAlchemyCatalog


@define(kw_only=True)
class TrinoCatalog(SQLAlchemyCatalog):
    """A collection of tables in a Trino catalog and schema."""

    user: str
    password: str
    host: str
    port: int
    catalog: str
    schema: str

    @cached_property
    def engine(self) -> Engine:
        return create_engine(self.url, pool_timeout=10)

    def detect_tables(self) -> None:
        trino_engine = self.engine

        with trino_engine.connect() as conn:

            for row in self._table_names(conn=conn):
                (table_name,) = row

                self._add_table_to_catalog(
                    table_name=table_name,
                    conn=conn,
                )

    def sample(self, table: Table, percentage: int = 10, **kwargs) -> MappingResult:
        assert table in self.tables, "Provided table does not belong to this catalog"

        fully_qualified_table_name = f"{self.catalog}.{self.schema}.{table.name}"
        sql = text(
            f"""
            SELECT * 
            FROM {fully_qualified_table_name} 
            TABLESAMPLE BERNOULLI({percentage})
        """
        )

        with self.engine.connect() as conn:
            return conn.execute(
                statement=sql,
            ).mappings()

    @property
    def url(self) -> URL:
        return URL(
            host=self.resolver.resolve(self.host),
            user=self.resolver.resolve(self.user),
            port=self.resolver.resolve(self.port),
            password=self.resolver.resolve(self.password),
            catalog=self.resolver.resolve(self.catalog),
            schema=self.resolver.resolve(self.schema),
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

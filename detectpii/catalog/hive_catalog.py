from typing import Sequence

from attrs import define
from sqlalchemy import Engine, create_engine, text, Connection, MappingResult

from detectpii.model import Catalog, Table, Column


@define(kw_only=True)
class HiveCatalog(Catalog):
    user: str
    password: str
    database: str
    schema: str
    port: str | int
    host: str

    @property
    def engine(self) -> Engine:
        return create_engine(self.url, connect_args={"auth": "LDAP"})

    def detect_tables(self) -> None:
        with self.engine.connect() as conn:
            for row in self._table_names(conn):
                (table_name,) = row

                self._add_table_to_catalog(
                    table_name=table_name,
                    conn=conn,
                )

    def sample(
        self, table: Table, percentage: int = 10, *args, **kwargs
    ) -> MappingResult:
        sql = text(
            f"""
                SELECT *
                FROM {table.name}
                WHERE RAND() <= {percentage / 100}
            """
        )

        with self.engine.connect() as conn:
            return conn.execute(
                statement=sql,
                parameters={
                    "percentage": percentage,
                },
            ).mappings()

    @property
    def url(self) -> str:
        return f"hive://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    def _table_names(self, conn: Connection):
        query = text("""SHOW TABLES""")
        return conn.execute(query)

    def _add_table_to_catalog(self, table_name: str, conn: Connection):
        query = text(f"DESC {table_name}")

        table = Table(
            name=table_name,
            columns=[Column(name=row[0]) for row in conn.execute(query)],
            schema="",
        )

        self.tables.append(table)

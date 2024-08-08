import itertools
from functools import cached_property

from attr import define
from sqlalchemy import Engine, create_engine, text, MappingResult

from detectpii.model import Catalog, Table, Column


@define(kw_only=True)
class SnowflakeCatalog(Catalog):
    """A collection of tables in a Snowflake database and schema."""

    user: str
    password: str
    account_identifier: str
    database: str
    schema: str

    @cached_property
    def engine(self) -> Engine:
        return create_engine(self.url)

    def detect_tables(self) -> None:
        with self.engine.connect() as conn:
            query = text(
                f"""
                SELECT table_name, column_name
                FROM information_schema.columns
                WHERE 1=1
                    AND LOWER(table_catalog) = LOWER('{self.database}')
                    AND LOWER(table_schema) = LOWER('{self.schema}')
                ORDER BY table_name, column_name
            """
            )

            rows = conn.execute(query)

            for table_name, table_rows in itertools.groupby(
                iterable=rows,
                key=lambda row: row[0],
            ):
                table = Table(
                    name=table_name,
                    schema=self.schema,
                    columns=[Column(name=table_row[-1]) for table_row in table_rows],
                )

                self.tables.append(table)

    def sample(
        self,
        table: Table,
        percentage: int = 10,
        *args,
        **kwargs,
    ) -> MappingResult:
        sql = text(f"""
            SELECT *
            FROM {table.name}
            TABLESAMPLE BERNOULLI(:percentage)
        """)

        with self.engine.connect() as conn:
            return conn.execute(
                statement=sql,
                parameters={
                    "percentage": percentage,
                },
            ).mappings()

    @property
    def url(self) -> str:
        return "snowflake://{user}:{password}@{account_identifier}/{database}/{schema}".format(
            user=self.resolver.resolve(self.user),
            password=self.resolver.resolve(self.password),
            account_identifier=self.resolver.resolve(self.account_identifier),
            database=self.resolver.resolve(self.database),
            schema=self.resolver.resolve(self.schema),
        )

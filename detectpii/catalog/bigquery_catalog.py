from collections.abc import Iterator

from attrs import define
from google.cloud import bigquery

from detectpii.model import Catalog, Table, Column


@define(kw_only=True)
class BigQueryCatalog(Catalog):
    project: str
    dataset: str

    def detect_tables(self) -> None:
        client = bigquery.Client(project=self.project)  # noqa

        for tablelistitem in client.list_tables(dataset=self.dataset):
            table = client.get_table(tablelistitem)
            self._add_table_to_catalog(table=table)

        client.close()

    def sample(self, table: Table, percentage: int = 10, *args, **kwargs) -> Iterator[dict]:
        client = bigquery.Client(project=self.project)  # noqa
        fully_qualified_name = f"{table.schema}.{table.name}"

        query = f"""
            SELECT *
            FROM {fully_qualified_name}
            TABLESAMPLE SYSTEM ({percentage} PERCENT)
        """

        iterator = (
            {column: value for column, value in row.items()}
            for row in client.query(query)
        )

        client.close()

        return iterator

    def _add_table_to_catalog(self, table: bigquery.Table) -> None:
        t = Table(
            name=f"{table.table_id}",
            schema=f"{table.project}.{table.dataset_id}",
            columns=[Column(name=field.name) for field in table.schema]
        )

        self.tables.append(t)

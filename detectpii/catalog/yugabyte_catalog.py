from sqlalchemy import MappingResult, text

from detectpii.catalog import PostgresCatalog
from detectpii.model import Table


class YugabyteCatalog(PostgresCatalog):

    def sample(
        self,
        table: Table,
        percentage: int = 10,
        *args,
        **kwargs,
    ) -> MappingResult:
        sql = text(
            f"""
            SELECT *
            FROM {table.name}
            WHERE RANDOM() <= {percentage / 100}
        """
        )

        with self.engine.connect() as conn:
            return conn.execute(
                statement=sql,
                parameters={
                    "percentage": percentage,
                },
            ).mappings()
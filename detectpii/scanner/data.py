import pandas as pd
from attr import define

from detectpii.detector import ColumnValueRegexDetector
from detectpii.model import Catalog, PiiColumn, Scanner


@define(kw_only=True)
class DataScanner(Scanner):
    """Scan the table values for PII columns."""

    times: int = 1
    percentage: int = 10

    def scan(self, catalog: Catalog, **kwargs) -> list[PiiColumn]:
        pii_columns = []

        column_value_regex_detector = ColumnValueRegexDetector()

        for _ in range(self.times):
            for table in catalog.tables:
                sample: pd.DataFrame = catalog.sample(
                    table=table,
                    percentage=self.percentage,
                )

                for column in table.columns:
                    pii_type = column_value_regex_detector.detect(
                        column=column,
                        sample=sample,
                    )

                    if pii_type:
                        pii_column = PiiColumn(
                            table=table.name,
                            column=column.name,
                            pii_type=pii_type,
                        )

                        pii_columns.append(pii_column)

        return pii_columns

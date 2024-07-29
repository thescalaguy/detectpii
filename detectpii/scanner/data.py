import pandas as pd
from attr import define

from detectpii.detector import ColumnValueRegexDetector
from detectpii.model import Catalog, PiiColumn


@define(kw_only=True)
class DataScanner:
    """Scan the table values for PII columns."""

    def scan(
        self,
        catalog: Catalog,
        percentage: int = 10,
        times: int = 1,
        **kwargs,
    ) -> list[PiiColumn]:
        pii_columns = []

        column_value_regex_detector = ColumnValueRegexDetector()

        for _ in range(times):
            for table in catalog.tables:
                sample: pd.DataFrame = catalog.sample(
                    table=table,
                    percentage=percentage,
                )

                for column in table.columns:
                    pii_type = column_value_regex_detector.detect(
                        column=column, sample=sample
                    )

                    if pii_type:
                        pii_column = PiiColumn(
                            table=table.name,
                            column=column.name,
                            pii_type=pii_type,
                        )

                        pii_columns.append(pii_column)

        return pii_columns

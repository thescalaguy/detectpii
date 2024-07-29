from attr import define

from detectpii.detector import ColumnNameRegexDetector
from detectpii.model import PiiColumn, Scanner, Catalog


@define(kw_only=True)
class MetadataScanner(Scanner):
    """Scan the table schema for PII columns."""

    def scan(self, catalog: Catalog, **kwargs,) -> list[PiiColumn]:
        pii_columns = []

        column_name_regex_detector = ColumnNameRegexDetector()

        for table in catalog.tables:
            for column in table.columns:
                pii_type = column_name_regex_detector.detect(column)

                if pii_type:
                    pii_column = PiiColumn(
                        table=table.name,
                        column=column.name,
                        pii_type=pii_type,
                    )

                    pii_columns.append(pii_column)

        return pii_columns

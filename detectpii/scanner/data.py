from attr import define

from detectpii.detector import ColumnValueRegexDetector
from detectpii.detector import Detector
from detectpii.model import PiiColumn, Scanner, Column, Table


@define(kw_only=True)
class DataScanner(Scanner):
    """Scan the table values for PII columns."""

    column_value_regex_detector: Detector = ColumnValueRegexDetector()

    def scan(
        self,
        table: Table,
        column: Column,
        value: str,
        **kwargs,
    ) -> list[PiiColumn]:
        pii_columns = []

        pii_type = self.column_value_regex_detector.detect(
            column=column,
            sample=str(value),
        )

        if pii_type:
            pii_column = PiiColumn(
                table=table.name,
                column=column.name,
                pii_type=pii_type,
            )

            pii_columns.append(pii_column)

        return pii_columns

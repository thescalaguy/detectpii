from attr import define

from detectpii.detector import ColumnValueRegexDetector
from detectpii.detector.column_name_regex import Detector
from detectpii.model import Catalog, PiiColumn, Scanner, Column


@define(kw_only=True)
class DataScanner(Scanner):
    """Scan the table values for PII columns."""

    times: int = 1
    percentage: int = 10
    column_value_regex_detector: Detector = ColumnValueRegexDetector()

    def scan(self, catalog: Catalog, **kwargs) -> list[PiiColumn]:
        pii_columns = []

        # -- Repeat the process as many times as requested
        for _ in range(self.times):

            # -- One table at a time
            for table in catalog.tables:

                # -- One row at a time
                for row in catalog.sample(
                    table=table,
                    percentage=self.percentage,
                ):

                    # -- One column at a time
                    for column_name, value in row.items():
                        column = Column(name=column_name)

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

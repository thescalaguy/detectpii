import re

from attr import define, Factory
from detectpii.catalog import CatalogT
from detectpii.model import PiiColumn, Column
from detectpii.scanner import ScannerT, MetadataScanner, DataScanner


@define(kw_only=True)
class PiiDetectionPipeline:
    catalog: CatalogT
    scanners: list[ScannerT] = Factory(list)
    ignore_column_regex: str | None = None
    percentage: int = 10

    def scan(self) -> list[PiiColumn]:
        self.catalog.detect_tables()
        pii_columns = []

        pii_columns.extend(self._scan_data())
        pii_columns.extend(self._scan_metadata())

        if self.ignore_column_regex:
            return [
                pii_column
                for pii_column in pii_columns
                if not re.match(self.ignore_column_regex, pii_column.column)
            ]

        return list(set(pii_columns))

    @property
    def data_scanners(self) -> list[ScannerT]:
        return [
            scanner for scanner in self.scanners if isinstance(scanner, DataScanner)
        ]

    @property
    def metadata_scanners(self) -> list[ScannerT]:
        return [
            scanner for scanner in self.scanners if isinstance(scanner, MetadataScanner)
        ]

    def _scan_data(self) -> list[PiiColumn]:
        pii_columns = []

        if not self.data_scanners:
            return pii_columns

        for table in self.catalog.tables:
            for row in self.catalog.sample(
                table=table,
                percentage=self.percentage,
            ):
                for column, value in row.items():
                    for scanner in self.data_scanners:
                        pii_type = scanner.scan(
                            table=table,
                            column=Column(name=column),
                            value=str(value),
                        )

                        if pii_type:
                            pii_columns.extend(pii_type)

        return pii_columns

    def _scan_metadata(self) -> list[PiiColumn]:
        pii_columns = []

        if not self.metadata_scanners:
            return pii_columns

        for table in self.catalog.tables:
            for column in table.columns:
                for scanner in self.metadata_scanners:
                    pii_type = scanner.scan(
                        table=table,
                        column=column,
                    )

                    if pii_type:
                        pii_columns.extend(pii_type)

        return pii_columns

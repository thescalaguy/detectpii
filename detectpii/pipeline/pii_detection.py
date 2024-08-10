import re

from attr import define, Factory
from detectpii.catalog import CatalogT
from detectpii.model import PiiColumn
from detectpii.scanner import ScannerT


@define(kw_only=True)
class PiiDetectionPipeline:
    catalog: CatalogT
    scanners: list[ScannerT] = Factory(list)
    ignore_column_regex: str | None = None

    def scan(self) -> list[PiiColumn]:
        self.catalog.detect_tables()
        pii_columns = []

        for scanner in self.scanners:
            pii_columns.extend(scanner.scan(catalog=self.catalog))

        if self.ignore_column_regex:
            return [
                pii_column
                for pii_column in pii_columns
                if not re.match(self.ignore_column_regex, pii_column.column)
            ]

        return list(set(pii_columns))

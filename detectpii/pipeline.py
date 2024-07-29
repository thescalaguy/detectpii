from attr import define, Factory

from detectpii.model import Catalog, Scanner, PiiColumn


@define(kw_only=True)
class PiiDetectionPipeline:
    catalog: Catalog
    scanners: list[Scanner] = Factory(list)

    def scan(self) -> list[PiiColumn]:
        self.catalog.detect_tables()
        pii_columns = []

        for scanner in self.scanners:
            pii_columns.extend(scanner.scan(catalog=self.catalog))

        return list(set(pii_columns))

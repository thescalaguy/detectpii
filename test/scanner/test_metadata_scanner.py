from detectpii.catalog import TestCatalog
from detectpii.pii_type import Person, Address
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.scanner import MetadataScanner


def test_metadata_scanner():
    pipeline = PiiDetectionPipeline(
        catalog=TestCatalog(),
        scanners=[
            MetadataScanner(),
        ],
    )

    pii_columns = pipeline.scan()
    column_names = set(pii_column.column for pii_column in pii_columns)
    column_types = set(pii_column.pii_type for pii_column in pii_columns)

    assert column_names == {
        "name",
        "address",
    }

    assert column_types == {
        Person(),
        Address(),
    }

    assert len(pii_columns) == 2

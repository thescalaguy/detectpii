from detectpii.pii_type import Address
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.scanner import DataScanner
from test.catalog.sqlite_memory_catalog import SQLiteMemoryCatalog


def test_metadata_scanner():
    pipeline = PiiDetectionPipeline(
        catalog=SQLiteMemoryCatalog(),
        scanners=[
            DataScanner(),
        ],
    )

    pii_columns = pipeline.scan()
    column_names = set(pii_column.column for pii_column in pii_columns)
    column_types = set(pii_column.pii_type for pii_column in pii_columns)

    assert column_names == {
        "address",
    }

    assert column_types == {
        Address(),
    }

    assert len(pii_columns) == 1

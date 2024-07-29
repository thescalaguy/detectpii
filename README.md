# 🔍 Detect PII

Detect PII is a library inspired by [piicatcher](https://github.com/tokern/piicatcher) and [CommonRegex](https://github.com/madisonmay/CommonRegex) to detect columns in tables that may potentially contain PII. It does so by performing regex matches 
on column names and column values, flagging the ones that may contain PII.

## Usage

### Check the table schema and values for PII columns
```python
from detectpii.catalog import PostgresCatalog
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.scanner import DataScanner, MetadataScanner

pg_catalog = PostgresCatalog(
    host="localhost",
    user="postgres",
    password="my-secret-pw",
    database="postgres",
    port=5432,
    schema="public"
)

pipeline = PiiDetectionPipeline(
    catalog=pg_catalog,
    scanners=[
        MetadataScanner(),
        DataScanner(),
    ]
)

pii_columns = pipeline.scan()
```

## Supported databases / warehouses  

* Postgres
* Trino

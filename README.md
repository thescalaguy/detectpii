# 🔍 Detect PII

Detect PII is a library inspired by [piicatcher](https://github.com/tokern/piicatcher) to detect columns in tables that may potentially contain PII. It does so by performing regex matches 
on column names, and flagging the ones that may contain PII.

## Usage 

```python
from detectpii.catalog import PostgresCatalog
from detectpii.scanner import PiiScanner

# -- Connect to your database
catalog = PostgresCatalog(
    host="localhost",
    user="postgres",
    password="my-secret-pw",
    database="postgres",
    port=5432,
    schema="public"
)

# -- Find the tables
catalog.detect_tables()

# -- Scan the tables for potentially PII columns
scanner = PiiScanner()
pii_columns = scanner.scan(catalog=catalog)
```  

## Supported databases / warehouses  

* Postgres
* Trino

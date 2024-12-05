# 🔍 Detect PII

Detect PII is a library inspired by [piicatcher](https://github.com/tokern/piicatcher) and [CommonRegex](https://github.com/madisonmay/CommonRegex) to detect columns in tables that may potentially contain PII. It does so by performing regex matches 
on column names and column values, flagging the ones that may contain PII.

## Usage

### Installation

Packages can be installed by specifying [extras](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies), e.g.:

```shell
pip install detectpii[postgres]
```

See all supported [databases and data warehouses](#supported-databases--warehouses).

### Scan tables for PII

```python
from detectpii.catalog import PostgresCatalog
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.scanner import DataScanner, MetadataScanner
from detectpii.util import print_columns

# -- Create a catalog to connect to a database / warehouse
pg_catalog = PostgresCatalog(
    host="localhost",
    user="postgres",
    password="my-secret-pw",
    database="postgres",
    port=5432,
    schema="public"
)

# -- Create a pipeline to detect PII in the tables
pipeline = PiiDetectionPipeline(
    catalog=pg_catalog,
    scanners=[
        MetadataScanner(),
        DataScanner(),
    ],
    times=1,
    percentage=20,
)

# -- Scan for PII columns.
pii_columns = pipeline.scan()

# -- Print them to the console
print_columns(pii_columns)
```

### Persist the pipeline

```python
import json
from detectpii.pipeline import pipeline_to_dict

# -- Create a pipeline
pipeline = ...

# -- Convert it into a dictionary
dictionary = pipeline_to_dict(pipeline)

# -- Print it
print(json.dumps(dictionary, indent=4))

# {
#     "catalog": {
#         "tables": [],
#         "resolver": {
#             "name": "PlaintextResolver",
#             "_type": "PlaintextResolver"
#         },
#         "user": "postgres",
#         "password": "my-secret-pw",
#         "host": "localhost",
#         "port": 5432,
#         "database": "postgres",
#         "schema": "public",
#         "_type": "PostgresCatalog"
#     },
#     "scanners": [
#         {
#             "_type": "MetadataScanner"
#         },
#         {
#             "_type": "DataScanner"
#         }
#     ]
#    "times": 1,
#    "percentage": 10
# }
```

### Load the pipeline

```python
from detectpii.pipeline import dict_to_pipeline

# -- Load the persisted pipeline as a dictionary
dictionary: dict = ...

# -- Convert it back to a pipeline object
pipeline = dict_to_pipeline(dictionary=dictionary)
```

For more detailed documentation, please see the `docs` folder.

## Supported databases / warehouses

| Database / Warehouse | Package              |
|----------------------|----------------------|
| Hive                 | detectpii[hive]      |
| Postgres             | detectpii[postgres]  |
| Snowflake            | detectpii[snowflake] |
| Trino                | detectpii[trino]     |
| Yugabyte             | detectpii[yugabyte]  |
| BigQuery             | detectpii[bigquery]  |

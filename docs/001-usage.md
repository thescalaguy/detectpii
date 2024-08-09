Using the library to detect PII requires setting up a PII detection pipeline. The pipeline takes a catalog, and a list of scanners. 
Once this is done, simply call the `scan` method of the pipeline to find columns that may contain PII. 

The general recipe for setting up a pipeline is as follows.  

```python
from detectpii.model import Catalog, Scanner, PiiColumn
from detectpii.pipeline import PiiDetectionPipeline

catalog: Catalog = ...

scanners: list[Scanner] = ...

pipeline: PiiDetectionPipeline = PiiDetectionPipeline(
    catalog=catalog,
    scanners=scanners
)

pii_columns: list[PiiColumn] = pipeline.scan()
```  

Each database or warehouse has its own catalog and requires different options to instantiate it. Similarly, each scanner 
has its own set of options.

# Catalogs  

The following sections show how to instantiate different catalogs.

## Postgres

```python
from detectpii.catalog import PostgresCatalog

catalog = PostgresCatalog(
    host="localhost",
    user="postgres",
    password="my-secret-pw",
    database="postgres",
    port=5432,
    schema="public"
)
```

## Snowflake 

```python
from detectpii.catalog import SnowflakeCatalog

catalog = SnowflakeCatalog(
    user="johndoe",
    password="my-secret-pw",
    database="people",
    schema="public",
    account_identifier="AE1V2M",
)
```  

## Trino  

```python
from detectpii.catalog import TrinoCatalog

catalog = TrinoCatalog(
    host="localhost",
    port=9080,
    user="admin",
    password="",
    catalog="hive",
    schema="views"
)
```  

## Yugabyte  

```python
from detectpii.catalog import YugabyteCatalog

catalog = YugabyteCatalog(
    host="localhost",
    user="yugabyte",
    password="yugabyte",
    database="yugabyte",
    port=5433,
    schema="public"
)
```

# Scanners  

The following sections show how to instantiate different scanners.  

## Metadata Scanner  

```python
from detectpii.scanner import MetadataScanner
scanner = MetadataScanner()
```

## Data Scanner

```python
from detectpii.scanner import DataScanner
scanner = DataScanner(times=1, percentage=10)
```
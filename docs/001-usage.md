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
has its own set of options. Please see the following sections for more information.

Pipelines can also be converted to, and from dictionary. The following example shows how to convert a pipeline to dictionary.

```python
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.pipeline import pipeline_to_dict

pipeline: PiiDetectionPipeline = ...
dictionary = pipeline_to_dict(pipeline)
```

Similarly, to load the pipeline from a dictionary, execute the following.

```python
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.pipeline import dict_to_pipeline

dictionary: dict = ...
pipeline: PiiDetectionPipeline = dict_to_pipeline(dictionary)
```

`Catalog`s also accept an instance of a `Resolver` which is used to resolve credentials for connecting to the database or warehouse. The 
following example shows how to use a resolver to fetch credentials from environment variables.

```python
from detectpii.catalog import PostgresCatalog
from detectpii.resolver import EnvironmentResolver

catalog = PostgresCatalog(
    user="USER",
    password="PASSWORD",
    schema="SCHEMA",
    host="HOST",
    port="PORT",
    database="DATABASE",
    resolver=EnvironmentResolver()
)
```

In the example above, the credentials passed are names of environment variables from which they will be fetched. By default, the catalog 
uses the `PlaintextResolver` which requires that the credentials be passed in plaintext.

# Catalogs  

The following sections show how to instantiate different catalogs.

## Hive Catalog

```python
from detectpii.catalog import HiveCatalog

catalog = HiveCatalog(
    user="scott",
    password="tiger",
    host="localhost",
    port=10000,
    database="default",
    schema="default",
)
```

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

# Resolvers  

The following sections show how to use different resolvers.

## PlaintextResolver

```python
from detectpii.catalog import PostgresCatalog
from detectpii.resolver import PlaintextResolver

catalog = PostgresCatalog(
    user="postgres",
    password="my-secret-pw",
    schema="public",
    host="localhost",
    port=5432,
    database="postgres",
    resolver=PlaintextResolver()
)
```

## EnvironmentResolver

```python
from detectpii.catalog import PostgresCatalog
from detectpii.resolver import EnvironmentResolver

catalog = PostgresCatalog(
    user="USER",
    password="PASSWORD",
    schema="SCHEMA",
    host="HOST",
    port="PORT",
    database="DATABASE",
    resolver=EnvironmentResolver()
)
```
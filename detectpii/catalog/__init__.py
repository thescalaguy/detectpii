from .trino_catalog import TrinoCatalog
from .postgres_catalog import PostgresCatalog
from .yugabyte_catalog import YugabyteCatalog
from .snowflake_catalog import SnowflakeCatalog
from .hive_catalog import HiveCatalog
from .test_catalog import TestCatalog
from .bigquery_catalog import BigQueryCatalog


CatalogT = (
    PostgresCatalog
    | TrinoCatalog
    | YugabyteCatalog
    | SnowflakeCatalog
    | HiveCatalog
    | TestCatalog
    | BigQueryCatalog
)

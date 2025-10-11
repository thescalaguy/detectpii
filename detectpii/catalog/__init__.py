from .empty_catalog import EmptyCatalog

CatalogT = EmptyCatalog

try:
    from .trino_catalog import TrinoCatalog

    CatalogT = CatalogT | TrinoCatalog
except ImportError:
    ...

try:
    from .postgres_catalog import PostgresCatalog

    CatalogT = CatalogT | PostgresCatalog
except ImportError:
    raise

try:
    from .yugabyte_catalog import YugabyteCatalog

    CatalogT = CatalogT | YugabyteCatalog
except ImportError:
    ...

try:
    from .snowflake_catalog import SnowflakeCatalog

    CatalogT = CatalogT | SnowflakeCatalog
except ImportError:
    ...

try:
    from .hive_catalog import HiveCatalog

    CatalogT = CatalogT | HiveCatalog
except ImportError:
    ...

try:
    from .bigquery_catalog import BigQueryCatalog

    CatalogT = CatalogT | BigQueryCatalog
except ImportError:
    ...

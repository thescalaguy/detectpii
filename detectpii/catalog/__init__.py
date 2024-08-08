from .trino_catalog import TrinoCatalog
from .postgres_catalog import PostgresCatalog
from .yugabyte_catalog import YugabyteCatalog
from .snowflake_catalog import SnowflakeCatalog

CatalogT = PostgresCatalog | TrinoCatalog | YugabyteCatalog | SnowflakeCatalog

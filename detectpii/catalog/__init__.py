from .trino_catalog import TrinoCatalog
from .postgres_catalog import PostgresCatalog
from .yugabyte_catalog import YugabyteCatalog

CatalogT = PostgresCatalog | TrinoCatalog | YugabyteCatalog

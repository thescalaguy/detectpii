from .trino_catalog import TrinoCatalog
from .postgres_catalog import PostgresCatalog

CatalogT = PostgresCatalog | TrinoCatalog

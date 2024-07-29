from .metadata import MetadataScanner
from .data import DataScanner

ScannerT = MetadataScanner | DataScanner

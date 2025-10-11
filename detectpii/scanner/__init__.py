from .data import DataScanner
from .metadata import MetadataScanner

ScannerT = MetadataScanner | DataScanner

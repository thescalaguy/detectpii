from cattrs import Converter
from cattrs.strategies import configure_tagged_union

from detectpii.catalog import CatalogT
from detectpii.pipeline import PiiDetectionPipeline
from detectpii.scanner import ScannerT


def pipeline_to_dict(pipeline: PiiDetectionPipeline) -> dict:
    """Convert a pipeline to a dictionary."""

    c = Converter()
    configure_tagged_union(ScannerT, c)
    configure_tagged_union(CatalogT, c)

    return c.unstructure(pipeline)


def dict_to_pipeline(dictionary: dict) -> PiiDetectionPipeline:
    """Convert a dictionary to a pipeline."""

    c = Converter()
    configure_tagged_union(ScannerT, c)
    configure_tagged_union(CatalogT, c)

    return c.structure(dictionary, PiiDetectionPipeline)

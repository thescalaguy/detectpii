from cattrs import Converter
from cattrs.strategies import configure_tagged_union

from detectpii.pipeline import PiiDetectionPipeline
from detectpii.scanner import ScannerT


def pipeline_to_json(pipeline: PiiDetectionPipeline) -> dict:
    c = Converter()
    configure_tagged_union(ScannerT, c)

    return c.unstructure(pipeline)

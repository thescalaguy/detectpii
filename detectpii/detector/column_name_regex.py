import abc
from typing import Optional

from attr import define, field

from detectpii.model import Column
from detectpii.pii_type import PiiType


@define(kw_only=True, frozen=True)
class Detector:

    @abc.abstractmethod
    def detect(
        self,
        column: Column,
        *args,
        **kwargs,
    ) -> Optional[PiiType]:
        raise NotImplementedError()


@define(kw_only=True, frozen=True)
class BaseColumnNameRegexDetector(Detector):
    regex: dict = field(factory=dict)

    def detect(
        self,
        column: Column,
        *args,
        **kwargs,
    ) -> Optional[PiiType]:
        for pii_type, ex in self.regex.items():
            if ex.match(column.name) is not None:
                return pii_type()

        return None

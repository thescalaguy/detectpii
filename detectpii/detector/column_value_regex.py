from typing import Optional

from attr import define, field

from detectpii.common_regex import CommonRegex, ENGLISH_COMMON_REGEXES
from detectpii.detector import Detector
from detectpii.model import Column
from detectpii.pii_type import (
    PiiType,
    Phone,
    Email,
    IPAddress,
    CreditCard,
    Address,
    ZipCode,
    PoBox,
    SSN,
)



import re


@define(kw_only=True)
class ColumnValueRegexDetector(Detector):
    """Detect PII columns by matching them against known patterns.

    This class has been borrowed from CommonRegex and modified for use with this library.
    """

    regex_patterns: dict[str, re.Pattern] = ENGLISH_COMMON_REGEXES
    
    def detect(
        self,
        column: Column,
        **kwargs,
    ) -> Optional[PiiType]:
        sample = kwargs["sample"]

        if not sample:
            return

        regex = CommonRegex(self.regex_patterns, str(sample))

        if regex.phones or regex.phones_with_exts:  # noqa
            return Phone()

        if regex.emails:  # noqa
            return Email()

        if regex.ips or regex.ipv6s:  # noqa
            return IPAddress()

        if regex.credit_cards:  # noqa
            return CreditCard()

        if regex.street_addresses:  # noqa
            return Address()

        if regex.zip_codes:  # noqa
            return ZipCode()

        if regex.po_boxes:  # noqa
            return PoBox()

        if regex.ssn_number:  # noqa
            return SSN()

        return None

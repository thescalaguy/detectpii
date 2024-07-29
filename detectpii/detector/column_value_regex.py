from typing import Optional

from attr import define

from detectpii.common_regex import CommonRegex
from detectpii.detector.column_name_regex import Detector
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


@define(kw_only=True)
class ColumnValueRegexDetector(Detector):
    """Detect PII columns by matching them against known patterns.

    This class has been borrowed from piicatcher and modified for use with this library.
    """

    def detect(
        self,
        column: Column,
        **kwargs,
    ) -> Optional[PiiType]:
        sample = kwargs["sample"]

        if not len(sample):
            return

        column_values = sample[column.name].astype(str).str.cat(sep=" ")
        regex = CommonRegex(column_values)

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

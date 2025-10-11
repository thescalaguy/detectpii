import re

from attrs import define

from detectpii.detector import BaseColumnNameRegexDetector
from detectpii.pii_type import Address
from detectpii.pii_type import BirthDate
from detectpii.pii_type import CreditCard
from detectpii.pii_type import Email
from detectpii.pii_type import Gender
from detectpii.pii_type import Nationality
from detectpii.pii_type import Password
from detectpii.pii_type import Person
from detectpii.pii_type import Phone
from detectpii.pii_type import PoBox
from detectpii.pii_type import SSN
from detectpii.pii_type import UserName
from detectpii.pii_type import ZipCode


@define(kw_only=True)
class EnglishColumnNameRegexDetector(BaseColumnNameRegexDetector):
    """Detect PII columns by matching them against known patterns.

    This class has been borrowed from piicatcher and modified for use with this library.
    """

    regex: dict = {
        Person: re.compile(
            "^.*(firstname|fname|lastname|lname|"
            "fullname|maidenname|_name|"
            "nickname|name_suffix|name|person).*$",
            re.IGNORECASE,
        ),
        Email: re.compile("^.*(email|e-mail|mail).*$", re.IGNORECASE),
        BirthDate: re.compile(
            "^.*(date_of_birth|dateofbirth|dob|"
            "birthday|date_of_death|dateofdeath|birthdate).*$",
            re.IGNORECASE,
        ),
        Gender: re.compile("^.*(gender).*$", re.IGNORECASE),
        Nationality: re.compile("^.*(nationality).*$", re.IGNORECASE),
        Address: re.compile(
            "^.*(address|city|state|county|country|zone|borough).*$",
            re.IGNORECASE,
        ),
        ZipCode: re.compile(
            "^.*(zipcode|zip_code|postal|postal_code|zip).*$",
            re.IGNORECASE,
        ),
        UserName: re.compile("^.*user(id|name|).*$", re.IGNORECASE),
        Password: re.compile("^.*pass.*$", re.IGNORECASE),
        SSN: re.compile(
            "^.*(ssn|social_number|social_security|"
            "social_security_number|social_security_no).*$",
            re.IGNORECASE,
        ),
        PoBox: re.compile("^.*(po_box|pobox).*$", re.IGNORECASE),
        CreditCard: re.compile(
            "^.*(credit_card|cc_number|cc_num|creditcard|"
            "credit_card_num|creditcardnumber).*$",
            re.IGNORECASE,
        ),
        Phone: re.compile(
            "^.*(phone|phone_number|phone_no|phone_num|"
            "telephone|telephone_num|telephone_no).*$",
            re.IGNORECASE,
        ),
    }

    name: str = "EnglishColumnNameRegexDetector"

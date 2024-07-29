from attr import define


@define(kw_only=True, frozen=True)
class PiiType:
    """A type of PII"""

    name: str
    type: str


@define(kw_only=True)
class Phone(PiiType):
    name: str = "Phone"
    type: str = "phone"


@define(kw_only=True)
class Email(PiiType):
    name: str = "Email"
    type: str = "email"


@define(kw_only=True)
class CreditCard(PiiType):
    name: str = "Credit Card"
    type: str = "credit_card"


@define(kw_only=True)
class Address(PiiType):
    name: str = "Address"
    type: str = "address"


@define(kw_only=True)
class Person(PiiType):
    name: str = "Person"
    type: str = "person"


@define(kw_only=True)
class BirthDate(PiiType):
    name: str = "Birth Date"
    type: str = "birth_date"


@define(kw_only=True)
class Gender(PiiType):
    name: str = "Gender"
    type: str = "gender"


@define(kw_only=True)
class Nationality(PiiType):
    name: str = "Nationality"
    type: str = "nationality"


@define(kw_only=True)
class SSN(PiiType):
    name: str = "SSN"
    type: str = "ssn"


@define(kw_only=True)
class ZipCode(PiiType):
    name: str = "Zip Code"
    type: str = "zip_code"


@define(kw_only=True)
class PoBox(PiiType):
    name: str = "PO Box"
    type: str = "po_box"


@define(kw_only=True)
class UserName(PiiType):
    name: str = "User Name"
    type: str = "user_name"


@define(kw_only=True)
class Password(PiiType):
    name: str = "word"
    type: str = "word"

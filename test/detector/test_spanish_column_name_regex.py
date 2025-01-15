from detectpii.detector.spanish_column_name_regex import SpanishColumnNameRegexDetector
from detectpii.model import Column
from detectpii.pii_type import *


def test_detect_person_pii_given_name_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="nombre")).__class__ == Person

def test_detect_email_pii_given_email_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="correo_electronico")).__class__ == Email

def test_detect_birthdate_pii_given_birthdate_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="fecha_nacimiento")).__class__ == BirthDate

def test_detect_gender_pii_given_gender_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="sexo")).__class__ == Gender

def test_detect_nationality_pii_given_nationality_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="nacionalidad")).__class__ == Nationality

def test_detect_address_pii_given_address_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="direccion")).__class__ == Address
    
def test_detect_zipcode_pii_given_zipcode_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="cp")).__class__ == ZipCode

def test_detect_username_pii_given_username_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="usuario")).__class__ == UserName

def test_detect_password_pii_given_password_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="contrasenia")).__class__ == Password

def test_detect_ssn_pii_given_ssn_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="dni")).__class__ == SSN

def test_detect_pobox_pii_given_pobox_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="casilla_correo")).__class__ == PoBox

def test_detect_creditcard_pii_given_creditcard_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="nro_tarjeta")).__class__ == CreditCard

def test_detect_phone_pii_given_phone_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(
        column=Column(name="telefono")).__class__ == Phone
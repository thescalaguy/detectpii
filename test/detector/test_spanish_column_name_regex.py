from detectpii.detector.spanish_column_name_regex import SpanishColumnNameRegexDetector
from detectpii.pii_type import Person


def test_detect_person_pii_given_name_like_column_name():
    assert SpanishColumnNameRegexDetector().detect(column="nombre") == Person
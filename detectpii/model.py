import abc
from typing import Sequence

from attr import define, Factory
from sqlalchemy import Engine

from detectpii.pii_type import PiiType
from detectpii.resolver import ResolverT, PlaintextResolver


@define(kw_only=True)
class Column:
    """A column in a table."""

    name: str


@define(kw_only=True)
class Table:
    """A table in the database or data warehouse."""

    name: str
    schema: str
    columns: list[Column]


@define(kw_only=True)
class Catalog:
    """A collection of tables."""

    tables: list[Table] = Factory(list)
    resolver: ResolverT = PlaintextResolver()

    @abc.abstractmethod
    def engine(self) -> Engine:
        raise NotImplementedError()

    @abc.abstractmethod
    def detect_tables(self) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def sample(self, table: Table, *args, **kwargs) -> Sequence[dict]:
        raise NotImplementedError()


@define(kw_only=True)
class Scanner:
    """A PII scanner."""

    @abc.abstractmethod
    def scan(self, *args, **kwargs):
        raise NotImplementedError()


@define(kw_only=True, frozen=True)
class PiiColumn:
    """A column that may potentially store PII data."""

    table: str
    column: str
    pii_type: PiiType

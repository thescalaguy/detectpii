from tabulate import tabulate

from detectpii.model import PiiColumn


def print_columns(pii_columns: list[PiiColumn]) -> None:
    rows = [
        [column.table, column.column, column.pii_type.name] for column in pii_columns
    ]

    print(tabulate(rows, headers=["Table", "Column", "Type"]))

import pprint

import pandas as pd

my_file_csv = "transactions.csv"
my_file_excel = "transactions_excel.xlsx"


def reading_csv(file_csv: str) -> None:
    """Считывание операций с CSV"""
    df_csv = pd.read_csv(file_csv, sep=";", dtype={"id": "str", "amount": "str"})
    list_of_dicts = df_csv.to_dict("records")

    return pprint.pprint(list_of_dicts, indent=4, width=80, sort_dicts=False)


def reading_excel(file_excel: str) -> None:
    """Считывание операций с .xlsx"""

    df_excel = pd.read_excel(file_excel, dtype={"id": "str", "amount": "str"})
    list_of_dicts = df_excel.to_dict("records")

    return pprint.pprint(list_of_dicts, indent=4, width=80, sort_dicts=False)


reading_csv(my_file_csv)
reading_excel(my_file_excel)

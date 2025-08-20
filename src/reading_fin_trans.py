import pandas as pd

my_file_csv = "transactions_excel.xlsx"
my_file_excel = "transactions.csv"


def reading_csv(file_csv: str) -> list:
    """Считывание операций с CSV"""
    try:
        df_csv = pd.read_csv(file_csv, sep=";", dtype={"id": "str", "amount": "str"})
        list_of_dicts = df_csv.fillna("None").to_dict("records")

        return list_of_dicts
    except UnicodeDecodeError:
        return ["Не правильный формат файла"]


def reading_excel(file_excel: str) -> list:
    """Считывание операций с .xlsx"""
    try:
        df_excel = pd.read_excel(file_excel, dtype={"id": "str", "amount": "str"})
        list_of_dicts = df_excel.to_dict("records")

        return list_of_dicts
    except UnicodeDecodeError:
        return ["Не правильный формат файла"]

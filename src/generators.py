from typing import Any, Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[Any, Any, None]:
    """Функция фильтрует список по наименованию валюты"""
    for x in transactions:
        if x["operationAmount"]["currency"]["code"] == currency:
            yield x
    while True:
        yield "Список пустой, итерировать нечего!"

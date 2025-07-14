from typing import Any, Generator


def filter_by_currency(transactions: list, currency: str) -> Generator[Any, Any, None]:
    """Функция фильтрует список по наименованию валюты"""
    for x in transactions:
        if x["operationAmount"]["currency"]["code"] == currency:
            yield x
    while True:
        yield "Список пустой, итерировать нечего!"


def transaction_descriptions(transactions: list) -> Generator[str | Any, Any, None]:
    """Функция возвращает тип операции"""
    for x in transactions:
        description = x.get("description", "")
        if description.isspace() or not description:
            yield f'ID операции где не найдено описание: {x["id"]}'
        else:
            yield description

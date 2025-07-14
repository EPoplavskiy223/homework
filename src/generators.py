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


def card_number_generator(start: int, stop: int) -> Generator[str, None]:
    """Функция генерирует номера карт с начального до конечного значения"""
    max_card_number = 9999999999999999
    number_cart = -1
    start_of_counting_cart = start + number_cart

    if start > stop:
        yield "Начальное значение не может быть больше конечного!"

    elif stop > max_card_number:
        yield f"Конечное значение не может превышать {max_card_number}!"

    else:
        for add in range(start, stop + 1):
            start_of_counting_cart += 1
            formatted = f"{start_of_counting_cart:016}"
            result = " ".join([formatted[i : i + 4] for i in range(0, 16, 4)])
            yield result

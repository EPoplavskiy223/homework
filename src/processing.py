from typing import Any


def filter_by_state(database: list[dict], state: str = "EXECUTED") -> list[Any]:
    """Сортирует список по ключу state"""
    filter = []
    for item in database:
        if item.get("state") == state:
            filter.append(item)
    return filter


def sort_by_date(database: list[dict], reverse: bool = True) -> list[dict]:
    """Сортировка словаря по дате"""
    sort_date = sorted(database, key=lambda x: x["date"], reverse=reverse)
    return sort_date

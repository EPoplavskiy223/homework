from typing import Any


def filter_by_state(database: list[dict], state: str = "EXECUTED") -> list[Any]:
    """Сортирует список по ключу state"""
    filter = []
    for item in database:
        if item.get("state") == state:
            filter.append(item)
    return filter

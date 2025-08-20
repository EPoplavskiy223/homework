import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Рекурсивный поиск по всем уровням вложенности"""

    pattern = re.compile(search, re.IGNORECASE)
    result = []

    def search_in_dict(d):
        for v in d.values():
            if isinstance(v, str) and pattern.search(v):
                return True
            elif isinstance(v, dict) and search_in_dict(v):
                return True
        return False

    for transaction in data:
        if search_in_dict(transaction):
            result.append(transaction)

    return result


def process_bank_operations(data):
    """Подсчет количества словарей в списке"""

    counter = Counter(['score' for _ in data])
    return counter
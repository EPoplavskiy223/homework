import re
from collections import Counter, defaultdict
from pprint import pprint

from reading_fin_trans import reading_csv

file = reading_csv("transactions.csv")


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Выполняет поиск по значению"""
    pattern = re.compile(search, re.IGNORECASE)
    filter_search = []

    for transaction in data:
        for key, value in transaction.items():
            if pattern.search(value):
                filter_search.append(transaction)
    return filter_search


# print(process_bank_search(file, "Открытие вклада"))


# def process_bank_operations(data, categories):
#     """Фильтрует категории"""
#
#     # category = process_bank_search(data, categories)
#     #
#     # for c in category:
#     #
#     #     counter = Counter(c)
#     #
#     # print(counter)
#
#
#
#     value_all = defaultdict(list)
#
#     for data_dict in data:
#         # category = data_dict['description']
#         for category in data_dict.values():
#             if category == categories:
#                 value_all[category].append(data_dict)
#                 counter = Counter(value_all)
#     # print(counter)
#     # print(type(value_all))
#     pprint(
#         counter,
#         indent=2,
#         width=80,
#         sort_dicts=False
#            )
#
#
# print(process_bank_operations(file, 'Открытие вклада'))

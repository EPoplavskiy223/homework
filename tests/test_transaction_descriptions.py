import pytest

from src.generators import transaction_descriptions

transactions = [
    {"id": 939719570, "description": "Перевод организации"},
    {"id": 895315941, "description": "Перевод с карты на карту"},
    {"id": 873106923, "description": "Перевод со счета на счет"},
    {"id": 142264268, " ": "Перевод со счета на счет"},
    {"id": 594226727, "description": " "},
]


@pytest.fixture
def transactions_fixture() -> list:
    return transactions


func = transaction_descriptions(transactions)


def test_transaction_descriptions_normal(transactions_fixture: list) -> None:
    """Нормальная работа функции"""
    assert next(func) == transactions_fixture[0]["description"]
    assert next(func) == transactions_fixture[1]["description"]
    assert next(func) == transactions_fixture[2]["description"]


def test_no_key() -> None:
    """Без ключа в списке"""
    assert next(func) == "ID операции где не найдено описание: 142264268"


def test_no_description() -> None:
    """Без значения в списке"""
    assert next(func) == "ID операции где не найдено описание: 594226727"

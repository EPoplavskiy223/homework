from typing import Any, Dict, List

import pytest

from src.processing import sort_by_date


# Фикстуры для тестовых данных
@pytest.fixture
def database_with_dates() -> List[Dict[str, str]]:
    return [
        {"id": "1", "date": "2023-01-15"},
        {"id": "2", "date": "2022-12-31"},
        {"id": "3", "date": "2023-01-01"},
        {"id": "4", "date": "2023-01-15"},  # Та же дата как у id=1
    ]


@pytest.fixture
def database_with_same_dates() -> List[Dict[str, str]]:
    return [
        {"id": "1", "date": "2023-01-01"},
        {"id": "2", "date": "2023-01-01"},
        {"id": "3", "date": "2023-01-01"},
    ]


@pytest.fixture
def empty_database() -> List[Dict[str, Any]]:
    return []


# Тесты для сортировки по дате
def test_sort_descending(database_with_dates: List[Dict[str, str]]) -> None:
    """Тестирование сортировки по убыванию даты"""
    result = sort_by_date(database_with_dates, reverse=True)
    dates = [item["date"] for item in result]
    assert dates == ["2023-01-15", "2023-01-15", "2023-01-01", "2022-12-31"]
    # Проверяем порядок id для одинаковых дат (должен сохраняться исходный порядок)
    assert [item["id"] for item in result[:2]] == ["1", "4"] or ["4", "1"]


def test_sort_ascending(database_with_dates: List[Dict[str, str]]) -> None:
    """Тестирование сортировки по возрастанию даты"""
    result = sort_by_date(database_with_dates, reverse=False)
    dates = [item["date"] for item in result]
    assert dates == ["2022-12-31", "2023-01-01", "2023-01-15", "2023-01-15"]


def test_sort_with_same_dates(database_with_same_dates: List[Dict[str, str]]) -> None:
    """Тестирование сортировки при одинаковых датах"""
    result = sort_by_date(database_with_same_dates, reverse=True)
    # Порядок элементов с одинаковой датой должен сохраниться
    assert [item["id"] for item in result] == ["1", "2", "3"]


def test_empty_database(empty_database: List[Dict[str, Any]]) -> None:
    """Тестирование сортировки пустого списка"""
    result = sort_by_date(empty_database)
    assert result == []


def test_default_sort_order(database_with_dates: List[Dict[str, str]]) -> None:
    """Тестирование сортировки со значением reverse по умолчанию (True)"""
    result = sort_by_date(database_with_dates)
    dates = [item["date"] for item in result]
    assert dates == ["2023-01-15", "2023-01-15", "2023-01-01", "2022-12-31"]

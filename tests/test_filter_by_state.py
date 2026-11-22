from typing import Any, Dict, List

import pytest

from src.processing import filter_by_state


# Фикстуры для тестовых данных
@pytest.fixture
def mixed_database() -> List[Dict[str, Any]]:
    return [
        {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
        {"id": "2", "state": "PENDING", "date": "2023-01-02"},
        {"id": "3", "state": "EXECUTED", "date": "2023-01-03"},
        {"id": "4", "state": "CANCELED", "date": "2023-01-04"},
    ]


@pytest.fixture
def executed_only_database() -> List[Dict[str, str]]:
    return [
        {"id": "1", "state": "EXECUTED", "date": "2023-01-01"},
        {"id": "3", "state": "EXECUTED", "date": "2023-01-03"},
    ]


@pytest.fixture
def empty_database() -> List[Dict[str, Any]]:
    return []


@pytest.fixture
def no_state_key_database() -> List[Dict[str, Any]]:
    return [
        {"id": "1", "date": "2023-01-01"},
        {"id": "2", "status": "PENDING", "date": "2023-01-02"},
    ]


@pytest.mark.parametrize(
    "state, expected_ids",
    [
        ("EXECUTED", ["1", "3"]),
        ("PENDING", ["2"]),
        ("CANCELED", ["4"]),
        ("UNKNOWN", []),
    ],
)
def test_filter_by_state_with_mixed_data(
    mixed_database: List[Dict[str, Any]], state: str, expected_ids: List[str]
) -> None:
    """Тестирование фильтрации с различными состояниями"""
    result = filter_by_state(mixed_database, state)
    assert [item["id"] for item in result] == expected_ids


def test_filter_by_state_with_executed_only(executed_only_database: List[Dict[str, str]]) -> None:
    """Тестирование с базой, где все записи EXECUTED"""
    result = filter_by_state(executed_only_database, "EXECUTED")
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_with_empty_database(empty_database: List[Dict[str, Any]]) -> None:
    """Тестирование с пустой базой данных"""
    result = filter_by_state(empty_database, "EXECUTED")
    assert result == []


def test_filter_by_state_default_state(mixed_database: List[Dict[str, Any]]) -> None:
    """Тестирование фильтрации со значением state по умолчанию (EXECUTED)"""
    result = filter_by_state(mixed_database)
    assert len(result) == 2
    assert all(item["state"] == "EXECUTED" for item in result)


def test_filter_by_state_with_no_state_key(no_state_key_database: List[Dict[str, Any]]) -> None:
    """Тестирование с записями, где отсутствует ключ state"""
    result = filter_by_state(no_state_key_database, "EXECUTED")
    assert result == []

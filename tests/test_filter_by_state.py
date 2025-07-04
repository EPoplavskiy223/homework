import pytest

from src.processing import filter_by_state

# Тестовые данные
test_data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Параметризованный тест для разных статусов
@pytest.mark.parametrize("state, expected_count", [
    ("EXECUTED", 2),
    ("CANCELED", 2),
    ("PENDING", 0),  # Тест для отсутствующего статуса
    ("COMPLETED", 0),  # Тест для другого отсутствующего статуса
])
def test_filter_by_state(state, expected_count):
    """Тестирует фильтрацию по разным статусам"""
    result = filter_by_state(test_data, state)
    assert len(result) == expected_count
    for item in result:
        assert item["state"] == state

# Тест для значения по умолчанию (EXECUTED)
def test_filter_by_state_default():
    """Тестирует фильтрацию со значением по умолчанию"""
    result = filter_by_state(test_data)
    assert len(result) == 2
    for item in result:
        assert item["state"] == "EXECUTED"

# Тест для пустого списка
def test_filter_by_state_empty_list():
    """Тестирует работу с пустым списком"""
    result = filter_by_state([], "EXECUTED")
    assert len(result) == 0
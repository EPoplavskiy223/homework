import pytest
from src.widget import get_date

@pytest.mark.parametrize("input_date,expected", [
    # Стандартные случаи
    ("2023-05-15T14:30:00.000", "15.05.2023"),
    ("2000-01-01T00:00:00.000", "01.01.2000"),
    # Граничные случаи
    ("9999-12-31T23:59:59.999", "31.12.9999"),
    ("0001-01-01T00:00:00.000", "01.01.0001"),
    # Разные времена (должны игнорироваться)
    ("2023-05-15T01:00:00.000", "15.05.2023"),
    ("2023-05-15T23:59:59.999", "15.05.2023"),
])
def test_valid_dates(input_date, expected):
    assert get_date(input_date) == expected


@pytest.mark.parametrize("invalid_date", [
    # Неполные даты
    "2023-05-15",
    "2023-05-15T14:30",
    # Неправильные форматы
    "15.05.2023",
    "May 15, 2023",
    "2023/05/15",
    # Пустая строка
    "",
    # Мусорные данные
    "not a date",
    "123456",
    None,
    123,
])
def test_invalid_dates(invalid_date):
    assert get_date(invalid_date) is None


def test_no_date_string():
    assert get_date("") is None
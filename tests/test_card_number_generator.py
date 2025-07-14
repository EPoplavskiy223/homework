import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize(
    "user_input_start, user_input_stop, expected",
    [
        (1, 3, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]),
        (1234567898765431, 1234567898765433, ["1234 5678 9876 5431", "1234 5678 9876 5432", "1234 5678 9876 5433"]),
    ],
)
def test_card_number_generator(user_input_start: int, user_input_stop: int, expected: str) -> None:
    """Тест корректных случаев"""
    result = list(card_number_generator(user_input_start, user_input_stop))
    assert result == expected


def test_max_value_exceeded() -> None:
    """Тест случая, когда значение превышает максимум"""
    func = card_number_generator(1, 99999999999999999)
    assert next(func) == "Конечное значение не может превышать 9999999999999999!"


def test_wrong_range() -> None:
    """Тест случая, когда start > stop"""
    func = card_number_generator(5, 2)
    assert next(func) == "Начальное значение не может быть больше конечного!"

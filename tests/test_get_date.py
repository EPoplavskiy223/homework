import pytest

from src.widget import get_date


@pytest.mark.parametrize(
    "user_input, expected",
    [
        ("2018-06-30T02:08:58.425572", "30.06.2018"),  # Для проверки
        ("2018-09-12", "Неверный формат!"),  # Для неверного формата
        ("", "Строка пустая!"),  # Для пустой строки
    ],
)
def test_get_date(user_input: str, expected: str) -> None:
    assert get_date(user_input) == expected

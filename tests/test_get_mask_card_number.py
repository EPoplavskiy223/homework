import pytest

from src.masks import get_mask_card_number


@pytest.fixture
def cart_number() -> str:
    return "7000 7922 8960 6311"


def test_mask_card_number(cart_number: str) -> None:
    masked_number = get_mask_card_number(cart_number)
    assert masked_number == "7000 79** **** 6311"


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),  # Для карт с 16 цифрами
        ("71583007347267", "7158 30** **72 67"),  # Для карт с 14 цифрами
        (" ", "Неверный формат карты"),  # Для пустой строки
        ("700079228960636", "Неверный формат карты"),  # Для неверного количества цифр
        ("Карта", "Неверный формат карты"),  # Для проверки цифр
    ],
)
def test_mask_card_number_parametrize(input_user: str, expected: str) -> None:
    assert get_mask_card_number(input_user) == expected

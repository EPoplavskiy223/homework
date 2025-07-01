import pytest

from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "original, expected",
    [
        ("5351711234567890", "5351 71** **** 7890"),
        ("Счет 4222222222222121", "Счет 42** **** **** 2121"),
        ("Счет 60111111111111", "Счет 60** **** **11 11"),
        ("37828224631000", "3782 82** **10 00"),
        ("1234567890", "Ошибка! Счет не найдет!"),
        ("", "Ошибка! Счет не найдет!"),
        ("Счет", "Ошибка! Счет не найдет!"),
    ],
)
def test_get_mask_card_number(original, expected):
    """Проверка маскировки номера карты."""
    masked = get_mask_card_number(original)
    assert masked == expected

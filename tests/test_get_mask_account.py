import pytest

from src.masks import get_mask_account

@pytest.mark.parametrize(
    "original, expected",
    [
         ('Счет 5351711234567890', '**7890'),
         ('Счет 4222222222222121', '**2121'),
         ('60111111111111', '**1111'),
         ('37828224631000', '**1000'),
         ("1234567890", "Ошибка! Счет не найдет!"),
         ("", "Ошибка! Счет не найдет!"),
         ("Счет", "Ошибка! Счет не найдет!")
    ])

def test_get_mask_account(original, expected):
    """ Маскировка счета """
    masked = get_mask_account(original)
    assert masked == expected
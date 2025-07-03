import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    'original, expected',
    [
        ('Счет 5351711234567890', 'Счет **7890'),
        ('Счет 4222222222222121', 'Счет **2121'),
        ('60111111111111', '6011 11** **** 1111'),
        ('37828224631000', ' 3782 82** **10 00'),
        ("1234567890", "Ошибка! Счет не найдет!"),
        ("", "Ошибка! Счет не найдет!"),
        ("Счет", "Ошибка! Счет не найдет!")

    ]
)

def test_mask_account_card(original, expected):
    """ Проверка отличия счета от карт """
    masked = mask_account_card(original)
    assert masked == expected
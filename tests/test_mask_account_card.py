import pytest

from src.widget import mask_account_card


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),  # Для карты с 16 цифрами
        ("MasterCard 71583007347267", "MasterCard 7158 30** **72 67"),  # Для карты с 14 цифрами
        ("Visa Classic 68319824767376581", "Неверный формат карты"),  # Для карты с некорректным количеством цифр
        ("Visa Platinum", "Строка с картой пустая!"),  # Для карты без цифр
        ("Счет 64686473678894779589", "Счет **9589"),  # Для счета с 20 цифрами
        ("Счет 7365410843013587430", "Неверный номер счета"),  # Для счета с некорректным количеством цифр
        ("Счет", "Неверный номер счета"),  # Для счета без цифр
        ("", "Строка пустая!"),  # Для пустой строки
    ],
)
def test_mask_account_cart(input_user: str, expected: str) -> None:
    assert mask_account_card(input_user) == expected

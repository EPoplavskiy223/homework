from typing import Union


def get_mask_card_number(number_cart: Union[int, str]) -> str:
    """Функция маскирует номер карты"""
    digit = []

    for i in number_cart:
        if i.isdigit():
            digit.append(i)

    result = []
    cart_str = str("".join(digit).replace(" ", ""))

    if len(cart_str) in (14, 16):

        masked = cart_str[0:6] + "*" * (len(cart_str[6:-4])) + cart_str[-4:]
        # Делает срез Карты и добавляет не замаскированные числа

        for i in range(0, len(masked), 4):  # Перебирает значения
            result.append(masked[i : i + 4])

        return " ".join(result)
    else:
        return "Неверный формат карты"


def get_mask_account(number_cart: Union[int, str]) -> str:
    """Функция маскирует номер счета '"""

    cart_str = str(number_cart).replace(" ", "")

    if len(cart_str) == 20:
        masked = "**" + cart_str[-4:]
        return masked
    else:
        return "Неверный формат счета"

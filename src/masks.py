from typing import Union


def get_mask_card_number(user_input: Union[int, str]) -> str:
    """Функция маскирует номер карты"""
    digit = []

    for i in user_input:
        if i.isdigit():
            digit.append(i)

    result = []
    cart_str = str("".join(digit).replace(" ", ""))

    if len(cart_str) == 0:
        return "Строка с картой пустая!"

    if len(cart_str) in (14, 16):

        masked = cart_str[0:6] + "*" * (len(cart_str[6:-4])) + cart_str[-4:]
        # Делает срез Карты и добавляет не замаскированные числа

        for i in range(0, len(masked), 4):  # Перебирает значения
            result.append(masked[i : i + 4])
        return " ".join(result)
    else:
        return "Неверный формат карты"


def get_mask_account(user_input: Union[int, str]) -> int | str:
    """Функция маскирует номер счета '"""
    digit = []

    for i in user_input:
        if i.isdigit():
            digit.append(i)

    cart_str = str("".join(digit).replace(" ", ""))
    if len(cart_str) == 20:
        masked = "**" + cart_str[-4:]
        return masked
    elif len(cart_str) > 20:
        return "Номер счета > 20 цифр"
    else:
        return "Номер счета < 20 цифр"

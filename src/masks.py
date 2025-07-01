from typing import Union


def get_mask_card_number(number_cart: Union[int, str]) -> Union[int, str]:
    """Функция маскирует по типу 'XXXX XX** **** XXXX'"""

    cart_str = str(number_cart).replace(" ", "")

    """ Счетчик кол-во цифр в вводных данных """
    cart_len = 0
    for char in cart_str:
        if char.isdigit():
            cart_len += 1

    """ Проверка наличия цифр """
    if cart_str == "" or cart_str == "Счет" or cart_len not in (14, 16):
        return "Ошибка! Счет не найдет!"

    """ Маскировка для вводных данных для 16 и 14 цифр """

    last_four = cart_str[-4:]
    front_six = cart_str[0:6]
    result_mask = []

    if cart_len == 16:
        mask = front_six + "*" * (cart_len - 10) + last_four
        if "Счет" in cart_str:
            mask = front_six + "*" * (cart_len - 6) + last_four
        for i in range(0, len(mask), 4):
            result_mask.append(mask[i : i + 4])
        return " ".join(result_mask)

    elif cart_len == 14:
        mask = front_six + "*" * (cart_len - 10) + last_four
        if "Счет" in cart_str:
            mask = front_six + "*" * (cart_len - 6) + last_four
        for i in range(0, len(mask), 4):
            result_mask.append(mask[i : i + 4])
        return " ".join(result_mask)

    else:
        return "Некорректный ввод. Счет слишком длинный"


def get_mask_account(number_cart: Union[int, str]) -> Union[int, str]:
    """Функция маскирует по типу '**XXXX'"""
    cart_str = str(number_cart)
    if len(cart_str) > 4:
        last_four = cart_str[-4:]
        mask = "*" * (len(cart_str[-6:]) - 4) + last_four
    return mask

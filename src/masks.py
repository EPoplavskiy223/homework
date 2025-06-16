from typing import Union


def get_mask_card_number(number_cart: Union[int, str]) -> Union[int, str]:
    """Функция маскирует по типу 'XXXX XX** **** XXXX'"""
    cart_str = str(number_cart)
    if len(cart_str) > 4:
        last_four = cart_str[-4:]
        front_six = cart_str[0:6]
        mask = front_six + "*" * (len(cart_str[5:-1]) - 4) + last_four
        result_mask = []
        for i in range(0, len(mask), 4):
            result_mask.append(mask[i : i + 4])

    return " ".join(result_mask)


def get_mask_account(number_cart: Union[int, str]) -> Union[int, str]:
    """Функция маскирует по типу '**XXXX'"""
    cart_str = str(number_cart)
    if len(cart_str) > 4:
        last_four = cart_str[-4:]
        mask = "*" * (len(cart_str[-6:]) - 4) + last_four
    return mask

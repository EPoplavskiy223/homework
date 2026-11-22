from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция обрабатывает информацию о карте и счёте"""
    if not user_input:
        return "Строка пустая!"

    mask_cart = get_mask_card_number(user_input)
    mask_account = get_mask_account(user_input)

    str_mask_cart = str(mask_cart)
    str_mask_account = str(mask_account)

    if "счет" in user_input.lower():
        if "Номер" in str_mask_account:
            return "Неверный номер счета"
        return f"Счет {mask_account}"
    if "Строка с картой пустая!" in str_mask_cart:
        return "Строка с картой пустая!"
    elif "Неверный формат карты" in str_mask_cart:
        return str_mask_cart
    else:
        return f"{''.join(i for i in user_input if i.isalpha() or i == ' ')}{mask_cart}"


def get_date(original_format_date: str) -> str:
    """Форматирует дату"""

    if not original_format_date:
        return "Строка пустая!"
    try:
        date_str = original_format_date.rstrip("Z")

        try:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")

        except ValueError:
            date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S")

        return date_obj.strftime("%d.%m.%Y")

    except ValueError:
        return "Неверный формат!"

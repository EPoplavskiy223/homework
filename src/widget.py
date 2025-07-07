from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_input: str) -> str:
    """Функция обрабатывает информацию о карте и счёте"""
    mask_cart = get_mask_card_number(user_input)
    mask_account = get_mask_account(user_input)
    if not user_input:
        return "Строка пустая!"

    if "счет" in user_input.lower():
        if "Номер" in mask_account:
            return "Неверный номер счета"
        return f"Счет {mask_account}"
    if "Строка с картой пустая!" in mask_cart:
        return "Строка с картой пустая!"
    elif "Неверный формат карты" in mask_cart:
        return mask_cart
    else:
        return f"{''.join(i for i in user_input if i.isalpha() or i == ' ')}{mask_cart}"


def get_date(original_format_date: str) -> str:
    """Форматирует дату"""

    if not original_format_date:
        return "Строка пустая!"
    try:
        date_obj = datetime.strptime(original_format_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")

    except ValueError:
        return "Неверный формат!"

from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_info: str) -> str:
    """Функция обрабатывает информацию о карте и счёте"""
    if "счет" in account_info.lower():
        return f"Счет {get_mask_account(account_info)}"
    else:
        return f"{''.join(i for i in account_info if i.isalpha() or i == ' ')}{get_mask_card_number(account_info)}"


def get_date(original_format_date: str) -> str:
    """Форматирует дату"""

    if not original_format_date:
        return "Строка пустая!"
    try:
        date_obj = datetime.strptime(original_format_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return "Неверный формат!"

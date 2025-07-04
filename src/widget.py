from datetime import datetime
from typing import Any, Optional

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_cart: str) -> str | tuple[str, int | str]:
    """Функция которая обрабатывает информацию о карте и счёте"""
    if "счет" in number_cart.lower().split()[0]:
        return f"Счет {get_mask_account(number_cart.split()[-1])}"
    else:
        return get_mask_card_number(number_cart.split()[-1])


def get_date(original_format_date: Any) -> Optional[str]:
    """Форматирует дату из формата '%Y-%m-%dT%H:%M:%S.%f' в '%d.%m.%Y'"""
    if not isinstance(original_format_date, str):
        return None
    try:
        date_obj = datetime.strptime(original_format_date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        return None

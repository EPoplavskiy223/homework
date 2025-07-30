import logging
import os
from typing import Union

os.makedirs("logs", exist_ok=True)

# Настройка логгера
logger = logging.getLogger("name")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# Создание дочерних логгеров
number_logger = logging.getLogger("name.mask_card")
account_logger = logging.getLogger("name.account_mask")


def get_mask_card_number(user_input: Union[int, str]) -> str:
    """Функция маскирует номер карты"""
    digit = []
    number_logger.info("Запуск функции")

    str_input = str(user_input)
    number_logger.info("Обработка карты")

    for i in str_input:
        if i.isdigit():
            digit.append(i)

    cart_str = "".join(digit).replace(" ", "")

    if len(cart_str) == 0:
        number_logger.error("Нет номера карты")
        return "Строка с картой пустая!"

    if len(cart_str) in (14, 16):
        masked = cart_str[:6] + ("*" * len(cart_str[6:-4])) + cart_str[-4:]
        number_logger.info("Маскировка карты")

        # Разбиваем на группы по 4 символа
        result = [masked[i : i + 4] for i in range(0, len(masked), 4)]
        number_logger.info("Форматирование карты")
        return " ".join(result)
    else:
        number_logger.error("Ошибка")
        return "Неверный формат карты"


def get_mask_account(user_input: Union[int, str]) -> Union[int, str]:
    """Функция маскирует номер счета"""
    account_logger.info("Запуск функции")
    digit = []
    str_input = str(user_input)

    for i in str_input:
        if i.isdigit():
            digit.append(i)
    account_logger.info("Обработка счета")
    cart_str = "".join(digit).replace(" ", "")

    if len(cart_str) == 20:
        masked = "**" + cart_str[-4:]
        account_logger.info("Маскировка счета")
        return masked
    elif len(cart_str) > 20:
        account_logger.error("Неверный формат")
        return "Номер счета > 20 цифр"
    else:
        account_logger.error("Неверный формат")
        return "Номер счета < 20 цифр"


if __name__ == "__main__":
    print(get_mask_card_number(1111222233334444))
    print(get_mask_account(12345678901234567890))

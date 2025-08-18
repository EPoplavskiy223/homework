import json
import logging
import os

os.makedirs("logs", exist_ok=True)

# Настройка логгера
logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


def convector_json(file_path: str) -> list | dict | str:
    """Конвертирует json файл"""
    try:
        logger.info("Запуск функции")
        with open(file_path, "r", encoding="utf-8") as json_file:
            logger.info(f"Файл {file_path} успешно открыт")
            data = json.load(json_file)
            logger.info("Файл успешно прочитан и преобразован в объект Python")
            return data  # type: ignore[no-any-return]

    except json.JSONDecodeError:
        logger.error("Не удалось прочитать файл")
        return "Файл пустой! Или не содержит .json"

    except FileNotFoundError:
        logger.error("Файл не найден")
        return "Файл не найден"

    # except json.JSONDecodeError or FileNotFoundError:
    #     return []


file_json = "C:/PythonProgramm/PROJECT/homework/data/operations.json"  # Почему-то принимает только абсолютный путь
import json


def convector_json(file_path: str) -> list | dict | str:
    """Конвертирует json файл"""
    try:
        with open(file_path, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            return data
    except json.JSONDecodeError:
        return "Файл пустой! Или не содержит .json"
    except FileNotFoundError:
        return "Файл не найден"
    # except json.JSONDecodeError or FileNotFoundError:
    #     return []


file_json = "C:/PythonProgramm/PROJECT/homework/data/operations.json"  # Почему-то принимает только абсолютный путь
print(convector_json(file_json))

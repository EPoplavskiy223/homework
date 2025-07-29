import os

import requests
from dotenv import load_dotenv


def currency_exchange(payload: dict) -> float | str:
    """Обмен валют из словаря в рубли"""

    url = "https://api.apilayer.com/exchangerates_data/convert"
    load_dotenv(".env")

    if not os.getenv("API_KEY_APILayer"):
        return "Ошибка: не найден API ключ"

    headers = {"apikey": os.getenv("API_KEY_APILayer")}

    payload.update({"to": "RUB"})

    response = requests.get(url, headers=headers, params=payload)
    status_code = response.status_code

    if status_code != 200:
        return f"Ошибка! Статус кода: {status_code}"

    return float(response.json()["result"])


payload = {
    "amount": "1",
    "from": "USD",
    # "to": "USD"
}
print(currency_exchange(payload))

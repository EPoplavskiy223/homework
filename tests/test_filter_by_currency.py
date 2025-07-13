from src.generators import filter_by_currency

original_currency = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]
incorrect_data = [{"operationAmount": {"currency": {"code": "USD"}}}]


def test_correct_test_operation_usd() -> None:
    """Тестирования в нормальных условиях USD"""
    func = filter_by_currency(original_currency, "USD")
    assert next(func) == original_currency[0]
    assert next(func) == original_currency[1]
    assert next(func) == original_currency[3]


def test_correct_test_operation_rub() -> None:
    """Тестирования в нормальных условиях RUB"""
    func = filter_by_currency(original_currency, "RUB")
    assert next(func) == original_currency[2]
    assert next(func) == original_currency[4]


def test_filter_by_currency_no_matches() -> None:
    """Тестирование случая, когда нет совпадений"""
    func = filter_by_currency(original_currency, "GBP")
    assert next(func) == "Список пустой, итерировать нечего!"


def test_filter_by_currency_empty_input() -> None:
    """Тестирование с пустым входным списком"""
    func = filter_by_currency([], "USD")
    assert next(func) == "Список пустой, итерировать нечего!"

from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

number_cart = "Счет 4222222222222121"
original_format_date = "2024-03-11T02:26:18.671407"
database = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

if __name__ == "__main__":
    print(get_mask_card_number(number_cart))

if __name__ == "__main__":
    print(get_mask_account(number_cart))

if __name__ == "__main__":
    print(mask_account_card(number_cart))

if __name__ == "__main__":
    print(get_date(original_format_date))

if __name__ == "__main__":
    print(filter_by_state(database))

if __name__ == "__main__":
    print(filter_by_state(database, "CANCELED"))

if __name__ == "__main__":
    print(sort_by_date(database))

if __name__ == "__main__":
    print(sort_by_date(database, False))

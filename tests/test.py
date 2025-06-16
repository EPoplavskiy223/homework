from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

number_cart = "Счет 35383033474447895560"
original_format_date = "2024-03-11T02:26:18.671407"

if __name__ == "__main__":
    print(get_mask_card_number(number_cart))

if __name__ == "__main__":
    print(get_mask_account(number_cart))

if __name__ == "__main__":
    print(mask_account_card(number_cart))

if __name__ == "__main__":
    print(get_date(original_format_date))

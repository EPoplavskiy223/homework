import pytest

from src.masks import get_mask_account


@pytest.mark.parametrize(
    "input_user, expected",
    [
        ("73654108430135874305", "**4305"),  # Для корректной работы
        ("7365410843013587430", "Номер счета < 20 цифр"),  # Для счетов состоящих не из 20 цифр
        ("736541084301358743011", "Номер счета > 20 цифр"),  # Для счетов состоящих не из 20 цифр
        (" ", "Номер счета < 20 цифр"),  # Для пустой строки
    ],
)
def test_get_mask_account(input_user: str, expected: str) -> None:
    assert get_mask_account(input_user) == expected

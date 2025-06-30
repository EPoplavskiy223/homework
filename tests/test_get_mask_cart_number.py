import pytest
from src.masks import get_mask_card_number

@pytest.mark.parametrize('original, expected', [
    ('5351711234567890', '5351 71** **** 7890'),
    ('4222222222222', '4222 2*** 2222'),
    ('6011111111111117', '6011 11** **** 1117'),
    ('378282246310005', '3782 822* **** 0005'),
    ('', '')
])
def test_get_mask_card_number(original, expected):
    """Проверка маскировки номера карты."""
    masked = get_mask_card_number(original)
    assert masked == expected
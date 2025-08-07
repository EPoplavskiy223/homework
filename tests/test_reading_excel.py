from io import BytesIO
from unittest.mock import patch

import pandas as pd
import pytest

from src.reading_fin_trans import reading_excel


@pytest.fixture
def mock_excel_data() -> bytes:

    data = {"id": ["1", "2"], "state": ["EXECUTED", "PENDING"], "amount": ["100", "200"], "currency": ["USD", "EUR"]}
    df = pd.DataFrame(data)

    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False)
    output.seek(0)
    return output.getvalue()


def test_reading_excel_with_mock() -> None:
    """Тест с моками без реального файла"""
    with patch("pandas.read_excel") as mock_read_excel, patch("pprint.pprint") as mock_pprint:
        mock_df = pd.DataFrame({"id": ["1", "2"], "amount": ["100", "200"]})
        mock_read_excel.return_value = mock_df

        reading_excel("dummy.xlsx")

        mock_read_excel.assert_called_once_with("dummy.xlsx", dtype={"id": "str", "amount": "str"})
        mock_pprint.assert_called_once()


def test_reading_excel_file_not_found() -> None:
    """Тест когда файл не существует"""
    with patch("os.path.isfile", return_value=False):
        with pytest.raises(FileNotFoundError):
            reading_excel("nonexistent.xlsx")

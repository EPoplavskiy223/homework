from pathlib import Path
from unittest.mock import mock_open, patch

import pandas as pd
import pytest

from src.reading_fin_trans import reading_csv

TEST_CSV_DATA = """id;state;date;amount;currency_name;currency_code;from;to;description
1;EXECUTED;2023-01-01;100;USD;840;Card 1234;Card 5678;Payment
2;PENDING;2023-02-02;200;EUR;978;Card 999;Account 123;Transfer"""


def test_reading_csv_with_mock() -> None:

    with patch("pandas.read_csv") as mock_read_csv, patch("pprint.pprint") as mock_pprint:

        mock_df = pd.DataFrame({"id": ["1", "2"], "state": ["EXECUTED", "PENDING"], "amount": ["100", "200"]})
        mock_read_csv.return_value = mock_df

        reading_csv("dummy.csv")

        mock_read_csv.assert_called_once_with("dummy.csv", sep=";", dtype={"id": "str", "amount": "str"})
        mock_pprint.assert_called_once()


def test_reading_csv_with_real_data() -> None:

    with patch("builtins.open", mock_open(read_data=TEST_CSV_DATA)):

        with patch("pprint.pprint") as mock_pprint:
            reading_csv("test.csv")

            args, _ = mock_pprint.call_args
            printed_data = args[0]

            assert len(printed_data) == 2
            assert printed_data[0]["id"] == "1"
            assert printed_data[1]["amount"] == "200"


@pytest.fixture
def csv_file(tmp_path: Path) -> str:
    file = tmp_path / "test.csv"
    file.write_text(TEST_CSV_DATA)
    return str(file)


def test_reading_csv_with_fixture(csv_file: str) -> None:
    # Тест с реальным файлом
    with patch("pprint.pprint") as mock_pprint:
        reading_csv(csv_file)
        mock_pprint.assert_called_once()

import unittest
from typing import Dict, Union
from unittest.mock import MagicMock, patch

from src.external_api import currency_exchange


class TestCurrencyExchange(unittest.TestCase):
    def setUp(self) -> None:
        self.payload: Dict[str, Union[int, str]] = {"amount": 1, "from": "USD"}

    @patch("os.getenv")
    @patch("requests.get")
    def test_currency_exchange(self, mock_requests_get: MagicMock, mock_os_getenv: MagicMock) -> None:
        """Успешное выполнение"""
        mock_os_getenv.return_value = "test_api_key"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 30.00}
        mock_requests_get.return_value = mock_response

        result = currency_exchange(self.payload)
        self.assertEqual(result, 30.00)

        mock_requests_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert",
            headers={"apikey": "test_api_key"},
            params={"amount": 1, "from": "USD", "to": "RUB"},
        )

    @patch("os.getenv")
    def test_no_api(self, mock_os_getenv: MagicMock) -> None:
        """Отсутствие API"""
        mock_os_getenv.return_value = None

        result = currency_exchange(self.payload)
        self.assertEqual(result, "Ошибка: не найден API ключ")

    @patch("os.getenv")
    @patch("requests.get")
    def test_no_json(self, mock_requests_get: MagicMock, mock_os_getenv: MagicMock) -> None:
        """Нет Json файла или некорректен"""
        mock_os_getenv.return_value = "test_api_key"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {}
        mock_requests_get.return_value = mock_response

        with self.assertRaises(KeyError):
            currency_exchange(self.payload)

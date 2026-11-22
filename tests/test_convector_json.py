import json
import unittest
from unittest.mock import mock_open, patch

from src.utils import convector_json


class TestConvectorJson(unittest.TestCase):
    def test_successful_json_load(self) -> None:
        """Успешно завершен"""
        test_data = {"key": "value"}
        json_str = json.dumps(test_data)

        with patch("builtins.open", mock_open(read_data=json_str)):
            result = convector_json("dummy_path.json")
            self.assertEqual(result, test_data)

    def test_file_not_found(self) -> None:
        """Файл не найден"""
        with patch("builtins.open", side_effect=FileNotFoundError()):
            result = convector_json("nonexistent_file.json")
            self.assertEqual(result, "Файл не найден")

    def test_empty_file(self) -> None:
        """Пустым файлом"""
        with patch("builtins.open", mock_open(read_data="")):
            with patch("json.load", side_effect=json.JSONDecodeError("msg", "doc", 0)):
                result = convector_json("empty.json")
                self.assertEqual(result, "Файл пустой! Или не содержит .json")

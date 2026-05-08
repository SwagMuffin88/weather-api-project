import unittest
from unittest.mock import patch

import requests

from weather_data import WeatherData
from weather_service import WeatherService


class TestWeatherApp(unittest.TestCase):

    def test_weather_data_creation(self):
        data = WeatherData("Tallinn", 15.5, "pilvine", 80)
        self.assertEqual(data.city, "Tallinn")
        self.assertEqual(data.temp, 15.5)
        self.assertEqual(str(data), f"--- Ilm: Tallinn ---\nTemperatuur: 15.5°C\nKirjeldus: Pilvine\nÕhuniiskus: 80%")

    @patch('requests.get')
    def test_fetch_weather_failure(self, mock_get):
        mock_get.return_value.status_code = 404

        # Defineerib kindla erindi, mis 404 response puhul ilmema peab
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()

        service = WeatherService("invalid_api_key")
        result = service.fetch_weather("Hawkins")

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
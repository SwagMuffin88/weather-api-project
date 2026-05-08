import requests
from weather_data import WeatherData


class WeatherService:
    """Weather service class for handling API requests."""

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'et'  # Vastused eesti keeles
        }

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()  # Kontrollib, kas tuli viga (nt 404)
            data = response.json()

            # Loome ja tagastame WeatherData objekti
            return WeatherData(
                city=data['name'],
                temp=data['main']['temp'],
                description=data['weather'][0]['description'],
                humidity=data['main']['humidity']
            )
        except Exception as e:
            print(f"Viga andmete pärimisel: {e}")
            return None
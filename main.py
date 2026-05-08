import os
from dotenv import load_dotenv
from weather_service import WeatherService

# Laeb andmed .env failist keskkonnamuutujatesse
load_dotenv()

class WeatherApp:
    """Main class for the weather service."""

    def __init__(self, api_key):
        self.service = WeatherService(api_key)

    def run(self):
        print("Tere tulemast ilmaennustajasse!")
        while True:
            city = input("\nSisesta linna nimi (või 'lõpeta'): ").strip()
            if city.lower() == 'lõpeta':
                break

            weather = self.service.fetch_weather(city)
            if weather:
                print(weather)
            else:
                print("Ilmaandmeid ei leitud. Proovi uuesti.")


if __name__ == "__main__":
    api_key = os.getenv("OPENWEATHER_API_KEY") # Kasutab võtit keskkonnamuutujast

    if not api_key:
        print("Viga: API võtit ei leitud .env failist!")
    else:
        app = WeatherApp(api_key)
        app.run()
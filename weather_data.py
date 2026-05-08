class WeatherData:
    """Class for carrying the weather data."""


    def __init__(self, city, temp, description, humidity):
        self.city = city
        self.temp = temp
        self.description = description
        self.humidity = humidity

    def __str__(self):
        return (f"--- Ilm: {self.city} ---\n"
                f"Temperatuur: {self.temp}°C\n"
                f"Kirjeldus: {self.description.capitalize()}\n"
                f"Õhuniiskus: {self.humidity}%")
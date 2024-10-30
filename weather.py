import pandas as pd
import requests


class Weather:
    def __init__(self, latitude, longitude, month, day, year):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.five_year_avg_temp = None
        self.five_year_min_temp = None
        self.five_year_max_temp = None
        self.five_year_avg_wind = None
        self.five_year_min_wind = None
        self.five_year_max_wind = None
        self.five_year_precip_sum = None
        self.five_year_min_precip = None
        self.five_year_max_precip = None

    # Define fetch_weather_data as part of the Weather class
    def fetch_weather_data(self, year, month, day):
        url = "https://archive-api.open-meteo.com/v1/archive"
        date_str = f"{year}-{month:02d}-{day:02d}"

        params = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "start_date": date_str,
            "end_date": date_str,
            "daily": ["temperature_2m_mean", "wind_speed_10m_max", "precipitation_sum"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/Chicago"
        }
        # Use the correct function to send the request
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            return data["daily"]  # Return only the temperature
        else:
            print("Failed to retrieve data")
            return None
    def temp_data(self):
        temperatures = {}
        for year in range(self.year, self.year - 5, -1):
            data = self.fetch_weather_data(year, self.month, self.day)
            if data and "temperature_2m_mean" in data:
                mean_temperature = data["temperature_2m_mean"][0]  # First element if list format
                temperatures[year] = mean_temperature
        return temperatures
    def wind_data(self):
        wind = {}
        for year in range(self.year, self.year - 5, -1):
            data = self.fetch_weather_data(year, self.month, self.day)
            if data and "wind_speed_10m_max" in data:
                max_wind = data["wind_speed_10m_max"][0]  # First element if list format
                wind[year] = max_wind
        return wind
    def precip_data(self):
        precip = {}
        for year in range(self.year, self.year - 5, -1):
            data = self.fetch_weather_data(year, self.month, self.day)
            if data and "precipitation_sum" in data:
                sum_precip = data["precipitation_sum"][0]  # First element if list format
                precip[year] = sum_precip
        return precip

weather = Weather(38.8339, -104.8214, 9, 30, 2024)
temperatures = weather.temp_data()
wind = weather.wind_data()
precip = weather.precip_data()
print(precip)

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
        temperature = []
        data = self.fetch_weather_data(self.year, self.month, self)
        if data:
            temperature.append(data)
            print(data)

weather = Weather(38.8339, -104.8214, 9, 30, 2024)
weather.temp_data()
    #
    # def temp_data(self):
    #     temperature = []
    #     for past_year in range(self.year -5, self.year):
    #         data = self.fetch_weather_data(past_year, self.month, self.day)
    #         if data:
    #             temperature.append(data["temperature_2m_mean"][0])
    #     if temperature:
    #         self.five_year_avg_temp = sum(temperature) / len(temperature)
    #         return self.five_year_avg_temp
    #
    # def wind_data(self):
    #     wind_speed = []
    #     for past_year in range(self.year -5, self.year):
    #         data = self.fetch_weather_data(past_year, self.month, self.day)
    #         if data:
    #             wind_speed.append(data["wind_speed_10m_max"][0])
    #     if wind_speed:
    #         self.five_year_max_wind = max(wind_speed)
    #         return self.five_year_max_wind
    # def precip_data(self):
    #     precipitation = []
    #     for past_year in range(self.year -5, self.year):
    #         data = self.fetch_weather_data(past_year, self.month, self.day)
    #         if data:
    #             precipitation.append(data["precipitation_sum"][0])
    #     if precipitation:
    #         self.five_year_avg_precip = sum(precipitation)
    #         return self.five_year_avg_precip


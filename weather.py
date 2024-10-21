
import openmeteo_requests
import requests

import requests_cache
from retry_requests import retry

from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

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
        # Ensure the date is formatted correctly
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
        for past_year in range(self.year -5, self.year):
            data = self.fetch_weather_data(past_year, self.month, self)
            if data:
                temperature.append(data["temperature_2m_mean"])
        if temperatures:
            self.five_year_avg_temp = sum(temperatures) / len(temperatures)
            return self.five_year_avg_temp

    def wind_data(self):
        wind_speed = []
        for past_year in range(self.year -5, self.year):
            data = self.fetch_weather_data(past_year, self)
            if data:
                wind_speed.append("wind_speed_10m_max")
        if wind_speed:
            self.five_year_avg_wind = max(wind_speed)
            return five_year_avg_wind
    def precip_data(self):
        precipitation = []
        for past_year in range(self.year -5, self.year):
            data = self.fetch_weather_data(past_year, self)
            if data:
                precipitation.append("precipitation_sum")
        if precipitation:
            self.five_year_avg_precip = sum(precipitation)
            return precipitation


# Instantiate the Weather class outside the class definition
weather = Weather(38.8339, -104.8214, 9, 30, 2024)

# Fetch data for a specific date and print the temperature
weather_init = weather.fetch_weather_data(2022, 9, 30)
print(f"Temperature on 2022-09-30: {five_year_avg_wind}, {precipitation}°F")
# # Setup the Open-Meteo API client with cache and retry on error
# cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
# retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
# openmeteo = openmeteo_requests.Client(session = retry_session)
#
# # Make sure all required weather variables are listed here
# # The order of variables in hourly or daily is important to assign them correctly below
# url = "https://archive-api.open-meteo.com/v1/archive"
# params = {
# 	"latitude": 38.8339,
# 	"longitude": -104.8214,
# 	"start_date": "2022-09-30",
# 	"end_date": "2022-09-30",
# 	"daily": ["temperature_2m_mean","wind_speed_10m_max","precipitation_sum"],
# 	"temperature_unit": "fahrenheit",
# 	"wind_speed_unit": "mph",
# 	"precipitation_unit": "inch",
# 	"timezone": "America/Chicago"
# }
# responses = openmeteo.weather_api(url, params=params)
#
# response = responses[0]

# methods to get mean precip
# def fetch_weather_data(self, year, month, day):
#
#     url = f"https://archive-api.open-meteo.com/v1/archive?latitude={self.latitude}longitude={self.longitude}&start_date={self.year}-{self.month}-{self.year}&end_date={self.year}-{self.month}-{self.year}&daily=temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FChicago}"
#     response = requests.get(url)
#
#     if response.status_code == 200:
#         data = response.json()
#         return data
#     else:
#         print("Failed to retrieve data")
#         return None
# #
# def get_mean_temp(self):
#     temperatures = []
#
#     for i in range(5):
#         year = self.year - i
#         weather_data = self.fetch_weather(year)
#         if weather_data:
#             temp = weather_data['forecast']['forecastday'][0]['day']['avgtemp_f']
#             temperatures.append(temp)
#         if temperatures:
#             self.avg_temp_5yr = sum(temperatures) / len(temperatures)
#             self.min_temp_5yr = min(temperatures)
#             self.max_temp_5yr = max(temperatures)
#             print(f"Mean Temperature over 5 years: {self.avg_temp_5yr}°F")
#             print(f"Min Temperature over 5 years: {self.min_temp_5yr}°F")
#             print(f"Max Temperature over 5 years: {self.max_temp_5yr}°F")
#
# location_weather = Weather(38.8339, -104.8214, 9, 30, 2024)
# location_weather.get_mean_temp()
# Base = sqlalchemy.orm.declarative_base()
#
# class WeatherData(Base):
#     __tablename__ = 'weather_data'
#     id = Column(Integer, primary_key=True)
#     latitude = Column(Float, nullable= False)
#     longitude = Column(Float,nullable= False)
#     month = Column(Integer, nullable= False)
#     day = Column(Integer, nullable= False)
#     year = Column(Integer, nullable= False)
#     five_year_avg_temp = Column(Float, nullable= True)
#     five_year_min_temp = Column(Float, nullable= True)
#     five_year_max_temp = Column(Float, nullable= True)
#     five_year_avg_wind = Column(Float, nullable= True)
#     five_year_min_wind = Column(Float, nullable= True)
#     five_year_max_wind = Column(Float, nullable= True)
#     five_year_sum_precip = Column(Float, nullable= True)
#     five_year_min_precip = Column(Float, nullable= True)
#     five_year_max_precip = Column(Float, nullable= True)
#
#     def __repr__(self):
#         return (f"<WeatherData(latitude={self.latitude}, longitude={self.longitude}, month={self.month}, "
#                 f"day={self.day}, year={self.year}, "
#                 f"five_year_avg_temp={self.five_year_avg_temp}, five_year_min_temp={self.five_year_min_temp}, "
#                 f"five_year_max_temp={self.five_year_max_temp}, five_year_avg_wind={self.five_year_avg_wind}, "
#                 f"five_year_min_wind={self.five_year_min_wind}, five_year_max_wind={self.five_year_max_wind}, "
#                 f"five_year_sum_precip={self.five_year_sum_precip}, five_year_min_precip={self.five_year_min_precip}, "
#                 f"five_year_max_precip={self.five_year_max_precip})>")
#
# # Database setup
# def setup_database(db_url='sqlite:///weather_data.db'):
#     engine = create_engine(db_url)
#     Base.metadata.create_all(engine)  # Create all tables in the engine
#     Session = sessionmaker(bind=engine)
#     return Session()
#
# # Example usage
# if __name__ == '__main__':
#     session = setup_database()
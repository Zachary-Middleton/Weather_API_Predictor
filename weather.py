
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
            data = self.fetch_weather_data(past_year, self.month, self.day)
            if data:
                temperature.append(data["temperature_2m_mean"][0])
        if temperature:
            self.five_year_avg_temp = sum(temperature) / len(temperature)
            return self.five_year_avg_temp

    def wind_data(self):
        wind_speed = []
        for past_year in range(self.year -5, self.year):
            data = self.fetch_weather_data(past_year, self.month, self.day)
            if data:
                wind_speed.append(data["wind_speed_10m_max"][0])
        if wind_speed:
            self.five_year_max_wind = max(wind_speed)
            return self.five_year_max_wind
    def precip_data(self):
        precipitation = []
        for past_year in range(self.year -5, self.year):
            data = self.fetch_weather_data(past_year, self.month, self.day)
            if data:
                precipitation.append(data["precipitation_sum"][0])
        if precipitation:
            self.five_year_avg_precip = sum(precipitation)
            return self.five_year_avg_precip


# Instantiate the Weather class outside the class definition
# Fetch and print temperature, wind, and precipitation data

weather = Weather(38.8339, -104.8214, 9, 30, 2024)

avg_temp = weather.temp_data()
max_wind = weather.wind_data()
avg_precip = weather.precip_data()

print(f"5-Year Average Temperature: {avg_temp:.2f}°F")
print(f"5-Year Max Wind Speed: {max_wind:.2f} mph")
print(f"5-Year Total Precipitation: {avg_precip:.2f} inches")



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
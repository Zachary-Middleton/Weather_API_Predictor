import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# Make sure all required weather variables are listed here
# The order of variables in hourly or daily is important to assign them correctly below
url = "https://archive-api.open-meteo.com/v1/archive"
params = {
	"latitude": 38.8339,
	"longitude": -104.8214,
	"start_date": "2022-09-30",
	"end_date": "2022-09-30",
	"daily": ["temperature_2m_mean","wind_speed_10m_max","precipitation_sum"],
	"temperature_unit": "fahrenheit",
	"wind_speed_unit": "mph",
	"precipitation_unit": "inch",
	"timezone": "America/Chicago"
}
responses = openmeteo.weather_api(url, params=params)

response = responses[0]
print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation {response.Elevation()} m asl")
print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")
# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_mean = daily.Variables(0).ValuesAsNumpy()
daily_precipitation_sum = daily.Variables(1).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(2).ValuesAsNumpy()

daily_data = {"date": pd.date_range(
	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = daily.Interval()),
	inclusive = "left"
)}
daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
daily_data["precipitation_sum"] = daily_precipitation_sum
daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max

daily_dataframe = pd.DataFrame(data = daily_data)
print(daily_dataframe)


#

# class Weather:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#         self.month = month
#         self.day_of_month = day
#         self.year = year
#         self.five_year_avg_temp = None
#         self.five_year_min_temp = None
#         self.five_year_max_temp = None
#         self.five_year_avg_wind = None
#         self.five_year_min_wind = None
#         self.five_year_max_wind = None
#         self.five_year_precip_sum = None
#         self.five_year_min_precip = None
#         self.five_year_max_precip = None
#





#     def weather_api(self, year):
#         # Adjusted URL for historical data
#         url = f'https://api.open-meteo.com/v1/historical?latitude={self.latitude}&longitude={self.longitude}&start_date={year}-10-19&end_date={year}-10-19&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum,wind_speed_10m_max&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch'
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print(f'Error fetching weather data for {year}: {response.status_code}')
#             return None
#
#     def calc_5year_data(self):
#         total_avg_temp = 0
#         total_max_temp = float('-inf')
#         total_min_temp = float('inf')
#         total_avg_wind = 0
#         total_max_wind = float('-inf')
#         total_min_wind = float('inf')
#         total_precip_sum = 0
#         total_min_precip = float('inf')
#         total_max_precip = float('-inf')
#         num_years = 5
#
#         # Iterate through the last 5 years
#         for year in range(datetime.now().year - 1, datetime.now().year - num_years - 1, -1):
#             data = self.weather_api(year)
#             if data and 'daily' in data:
#                 daily_data = data['daily']
#                 avg_temp = daily_data['temperature_2m_mean'][0]
#                 max_temp = daily_data['temperature_2m_max'][0]
#                 min_temp = daily_data['temperature_2m_min'][0]
#                 avg_wind = daily_data['wind_speed_10m_max'][0]
#                 precip_sum = daily_data['precipitation_sum'][0]
#
#                 total_avg_temp += avg_temp
#                 total_max_temp = max(total_max_temp, max_temp)
#                 total_min_temp = min(total_min_temp, min_temp)
#                 total_avg_wind += avg_wind
#                 total_max_wind = max(total_max_wind, avg_wind)
#                 total_min_wind = min(total_min_wind, avg_wind)
#                 total_precip_sum += precip_sum
#                 total_min_precip = min(total_min_precip, precip_sum)
#                 total_max_precip = max(total_max_precip, precip_sum)
#
#         self.five_year_avg_temp = total_avg_temp / num_years
#         self.five_year_max_temp = total_max_temp
#         self.five_year_min_temp = total_min_temp
#         self.five_year_avg_wind = total_avg_wind / num_years
#         self.five_year_max_wind = total_max_wind
#         self.five_year_min_wind = total_min_wind
#         self.five_year_precip_sum = total_precip_sum / num_years
#         self.five_year_min_precip = total_min_precip
#         self.five_year_max_precip = total_max_precip
#
#     def __str__(self):
#         return (f"Weather Data for ({self.latitude}, {self.longitude}):\n"
#                 f"Average Temp (last 5 years): {self.five_year_avg_temp:.2f}°F\n"
#                 f"Max Temp (last 5 years): {self.five_year_max_temp:.2f}°F\n"
#                 f"Min Temp (last 5 years): {self.five_year_min_temp:.2f}°F\n"
#                 f"Average Wind Speed (last 5 years): {self.five_year_avg_wind:.2f} mph\n"
#                 f"Max Wind Speed (last 5 years): {self.five_year_max_wind:.2f} mph\n"
#                 f"Min Wind Speed (last 5 years): {self.five_year_min_wind:.2f} mph\n"
#                 f"Average Precipitation (last 5 years): {self.five_year_precip_sum:.2f} inches\n"
#                 f"Min Precipitation (last 5 years): {self.five_year_min_precip:.2f} inches\n"
#                 f"Max Precipitation (last 5 years): {self.five_year_max_precip:.2f} inches")
#
# # Example usage:
# colorado_springs_weather.calc_5year_data()
# colorado_springs_weather = Weather(latitude=38.8339, longitude=-104.8214)
# print(colorado_springs_weather)

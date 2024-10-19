













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

# Process daily data. The order of variables needs to be the same as requested.
daily = response.Daily()
daily_temperature_2m_mean = daily.Variables(0).ValuesAsNumpy()
daily_wind_speed_10m_max = daily.Variables(1).ValuesAsNumpy()
daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()


print(daily_precipitation_sum)
print(daily_wind_speed_10m_max)
print(daily_temperature_2m_mean)
#
#
# daily_data = {"date": pd.date_range(
# 	start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
# 	end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
# 	freq = pd.Timedelta(seconds = daily.Interval()),
# 	inclusive = "left"
# )}
# daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
# daily_data["precipitation_sum"] = daily_precipitation_sum
# daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max
#
# daily_dataframe = pd.DataFrame(data = daily_data)
# print(daily_dataframe)
#

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





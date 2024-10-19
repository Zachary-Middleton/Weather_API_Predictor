
import openmeteo_requests

import requests_cache
from retry_requests import retry

from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy


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

Base = sqlalchemy.orm.declarative_base()

class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable= False)
    longitude = Column(Float,nullable= False)
    month = Column(Integer, nullable= False)
    day = Column(Integer, nullable= False)
    year = Column(Integer, nullable= False)
    five_year_avg_temp = Column(Float, nullable= True)
    five_year_min_temp = Column(Float, nullable= True)
    five_year_max_temp = Column(Float, nullable= True)
    five_year_avg_wind = Column(Float, nullable= True)
    five_year_min_wind = Column(Float, nullable= True)
    five_year_max_wind = Column(Float, nullable= True)
    five_year_sum_precip = Column(Float, nullable= True)
    five_year_min_precip = Column(Float, nullable= True)
    five_year_max_precip = Column(Float, nullable= True)
   
    def __repr__(self):
        return (f"<WeatherData(latitude={self.latitude}, longitude={self.longitude}, month={self.month}, "
                f"day={self.day}, year={self.year}, "
                f"five_year_avg_temp={self.five_year_avg_temp}, five_year_min_temp={self.five_year_min_temp}, "
                f"five_year_max_temp={self.five_year_max_temp}, five_year_avg_wind={self.five_year_avg_wind}, "
                f"five_year_min_wind={self.five_year_min_wind}, five_year_max_wind={self.five_year_max_wind}, "
                f"five_year_sum_precip={self.five_year_sum_precip}, five_year_min_precip={self.five_year_min_precip}, "
                f"five_year_max_precip={self.five_year_max_precip})>")

# Database setup
def setup_database(db_url='sqlite:///weather_data.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # Create all tables in the engine
    Session = sessionmaker(bind=engine)
    return Session()

# Example usage
if __name__ == '__main__':
    session = setup_database()
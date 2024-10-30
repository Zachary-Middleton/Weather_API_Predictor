
from weather import Weather  # Make sure this matches the filename of your Weather class
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker
import sqlalchemy
#
# 2024
weather2024 = Weather(38.8339, -104.8214, 9, 30, 2024)
temperature_data2024 = weather2024.temp_data()
wind_data2024 = weather2024.wind_data()
pricip_data2024 = weather2024.precip_data()
# print(temperature_data2024)
# print(wind_data2024)
# print(pricip_data2024)
#2023
weather2023 = Weather(38.8339, -104.8214, 9, 30, 2023)
temperature_data2023 = weather2023.temp_data()
wind_data2023 = weather2023.wind_data()
pricip_data2023 = weather2023.precip_data()

# 2022
weather2022 = Weather(38.8339, -104.8214, 9, 30, 2022)
temperature_data2022 = weather2022.temp_data()
wind_data2022 = weather2022.wind_data()
pricip_data2022 = weather2022.precip_data()

# 2021
weather2021 = Weather(38.8339, -104.8214, 9, 30, 2021)
temperature_data2021 = weather2021.temp_data()
wind_data2021 = weather2021.wind_data()
pricip_data2021 = weather2021.precip_data()

# 2020
weather2020 = Weather(38.8339, -104.8214, 9, 30, 2020)
temperature_data2020 = weather2020.temp_data()
wind_data2020 = weather2020.wind_data()
pricip_data2020 = weather2020.precip_data()

#statistics

def avg_temp(temperatures):
    average_temp = sum(temperatures)/ len(temperatures)
    return average_temp
def max_wind(wind):
    maximum_wind = max(wind)
    return maximum_wind
def precip_sum(precipitation):
    precipitation_sum = sum(precipitation)
    return precipitation_sum


# temperatures = [temperature_data2020, temperature_data2021, temperature_data2022, temperature_data2023, temperature_data2024]
# wind = [wind_data2020, wind_data2021,wind_data2022,wind_data2023,wind_data2024]
# precipitation = [pricip_data2020, pricip_data2021,pricip_data2022,pricip_data2023,pricip_data2024]
#
# print(avg_temp(temperatures))
# print(max_wind(wind))
# print(precip_sum(precipitation))
#
# Base = sqlalchemy.orm.declarative_base()
#
# class WeatherData(Base):
#     __tablename__ = 'weather_data'
#     id = Column(Integer, primary_key=True)
#     latitude = Column(Float, nullable=False)
#     longitude = Column(Float, nullable=False)
#     month = Column(Integer, nullable=False)
#     day = Column(Integer, nullable=False)
#     year = Column(Integer, nullable=False)
#     five_year_avg_temp = Column(Float, nullable=True)
#     five_year_min_temp = Column(Float, nullable=True)
#     five_year_max_temp = Column(Float, nullable=True)
#     five_year_avg_wind = Column(Float, nullable=True)
#     five_year_min_wind = Column(Float, nullable=True)
#     five_year_max_wind = Column(Float, nullable=True)
#     five_year_sum_precip = Column(Float, nullable=True)
#     five_year_min_precip = Column(Float, nullable=True)
#     five_year_max_precip = Column(Float, nullable=True)
#
#     def __init__(self, latitude, longitude, month, day, year,
#                  five_year_avg_temp=None, five_year_min_temp=None, five_year_max_temp=None,
#                  five_year_avg_wind=None, five_year_min_wind=None, five_year_max_wind=None,
#                  five_year_sum_precip=None, five_year_min_precip=None, five_year_max_precip=None):
#         self.latitude = latitude
#         self.longitude = longitude
#         self.month = month
#         self.day = day
#         self.year = year
#         self.five_year_avg_temp = five_year_avg_temp
#         self.five_year_min_temp = five_year_min_temp
#         self.five_year_max_temp = five_year_max_temp
#         self.five_year_avg_wind = five_year_avg_wind
#         self.five_year_min_wind = five_year_min_wind
#         self.five_year_max_wind = five_year_max_wind
#         self.five_year_sum_precip = five_year_sum_precip
#         self.five_year_min_precip = five_year_min_precip
#         self.five_year_max_precip = five_year_max_precip
#
#     def __repr__(self):
#         return (f"{self.id} {self.latitude} {self.longitude} {self.month} {self.day} {self.year} {self.five_year_avg_temp} {self.five_year_min_temp} {self.five_year_max_temp} {self.five_year_avg_wind} {self.five_year_min_wind} {self.five_year_min_wind} {self.five_year_max_wind} {self.five_year_sum_precip} {self.five_year_min_precip} {self.five_year_max_precip}")
#
#
# def setup_database(db_url='sqlite:///weather_data.db'):
#     engine = create_engine(db_url)
#     Base.metadata.create_all(engine)  # Create all tables in the engine
#     Session = sessionmaker(bind=engine)
#     return Session()
#
# session = setup_database()
# weather = Weather(38.8339, -104.8214, 9, 30, 2024)
# values_temp = list(temperature_data.values())
# values_wind = list(wind_data.values())
# values_precip = list(precip_data.values())
# precipitation_sum = precip_sum(precip_data)
# average_temp = avg_temp(temperature_data)
# maximum_wind = max_wind(wind_data)
# max_temp = float(max(values_temp))
# min_temp = float(min(values_temp))
# min_wind = float(min(values_wind))
# avg_wind = float(sum(values_wind) / len(values_wind))
# sum_precip = float(sum(values_precip))
# min_precip = float(min(values_precip))
# max_precip = float(max(values_precip))
#
# new_entry = WeatherData(
#     latitude=weather.latitude,
#     longitude=weather.longitude,
#     month=weather.month,
#     day = weather.day,
#     year = weather.year,
#     five_year_avg_temp = average_temp,
#     five_year_min_temp =  min_temp,
#     five_year_max_temp = max_temp,
#     five_year_avg_wind = avg_wind,
#     five_year_min_wind = min_wind,
#     five_year_max_wind = max_wind,
#     five_year_sum_precip = sum_precip,
#     five_year_min_precip = min_precip,
#     five_year_max_precip = max_precip,
# )
# session.add(new_entry)
# session.commit()
import weather
from weather import Weather  # Make sure this matches the filename of your Weather class
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker
import sqlalchemy
#
# # 2024
# weather2024 = Weather(38.8339, -104.8214, 9, 30, 2024)
# temperature_data2024 = weather2024.temp_data()
# wind_data2024 = weather2024.wind_data()
# pricip_data2024 = weather2024.precip_data()
# print(temperature_data2024)
# print(wind_data2024)
# print(pricip_data2024)
# #2023
# weather2023 = Weather(38.8339, -104.8214, 9, 30, 2023)
# temperature_data2023 = weather2023.temp_data()
# wind_data2023 = weather2023.wind_data()
# pricip_data2023 = weather2023.precip_data()
#
# # 2022
# weather2022 = Weather(38.8339, -104.8214, 9, 30, 2022)
# temperature_data2022 = weather2022.temp_data()
# wind_data2022 = weather2022.wind_data()
# pricip_data2022 = weather2022.precip_data()
#
# # 2021
# weather2021 = Weather(38.8339, -104.8214, 9, 30, 2021)
# temperature_data2021 = weather2021.temp_data()
# wind_data2021 = weather2021.wind_data()
# pricip_data2021 = weather2021.precip_data()
#
# # 2020
# weather2020 = Weather(38.8339, -104.8214, 9, 30, 2020)
# temperature_data2020 = weather2020.temp_data()
# wind_data2020 = weather2020.wind_data()
# pricip_data2020 = weather2020.precip_data()

#statistics

def avg_temp(temperatures):
    temp_2024= weather2024.temp_data()
    temp_2023= weather2023.temp_data()
    temp_2022= weather2022.temp_data()
    temp_2021= weather2021.temp_data()
    temp_2020= weather2020.temp_data()
    sum = temp_2024 + temp_2023 + temp_2022 + temp_2021 + temp_2020
    avg_temperature= sum/len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return avg_temperature, min_temp, max_temp
def max_wind(wind):
    wind_2024= weather2024.wind_data()
    wind_2023= weather2023.wind_data()
    wind_2022= weather2022.wind_data()
    wind_2021= weather2021.wind_data()
    wind_2020= weather2020.wind_data()
    sum = wind_2024 + wind_2023 + wind_2022 + wind_2021 + wind_2020
    avg_wind = sum/len(wind)
    min_wind = min(wind)
    max_wind = max(wind)
    return avg_wind, min_wind, max_wind
def sum_precip(precipitation):
    precipitation_2024= weather2024.precipitation_data()
    precipitation_2023= weather2023.precipitation_data()
    precipitation_2022= weather2022.precipitation_data()
    precipitation_2021= weather2021.precipitation_data()
    precipitation_2020= weather2020.precipitation_data()
    sum = precipitation_2024 + precipitation_2023 + precipitation_2022 + precipitation_2021 + precipitation_2020
    avg_precip= sum/len(precipitation)
    min_precip = min(precipitation)
    max_precip = max(precipitation)
    return avg_precip, min_precip, max_precip

temperatures = weather.temp_data()
wind = weather.wind_data()
precipitations = weather.precip_data

weather2024 = Weather(38.8339, -104.8214, 9, 30, 2024)
weather2023 = Weather(38.8339, -104.8214, 9, 30, 2023)
weather2022 = Weather(38.8339, -104.8214, 9, 30, 2022)
weather2021 = Weather(38.8339, -104.8214, 9, 30, 2021)
weather2020 = Weather(38.8339, -104.8214, 9, 30, 2020)

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
# # session = setup_database()
#
# average_temp = avg_temp(temperatures)
# max_temp = max(temperatures)
# min_temp = min(temperatures)
# min_wind = min(wind)
# avg_wind =  sum(wind) / len(wind)
# maximum_wind = max_wind(wind)
# sum_precip = precip_sum(precipitation)
# min_precip = min(precipitation)
# max_precip = max(precipitation)
#
# # print(maximum_wind)
#
# entry_2024 = WeatherData(
#     latitude=weather.latitude,
#     longitude=weather.longitude,
#     month=9,
#     day = 30,
#     year = 2024,

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
session.add(entry_2024)
session.commit()
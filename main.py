import weather
from weather import Weather  # Make sure this matches the filename of your Weather class
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker
import sqlalchemy


def avg_temp():
    temp_2024= weather2024.temp_data()
    temp_2023= weather2023.temp_data()
    temp_2022= weather2022.temp_data()
    temp_2021= weather2021.temp_data()
    temp_2020= weather2020.temp_data()
    temperatures = [temp_2024, temp_2023, temp_2022, temp_2021, temp_2020]
    avg_temperature = sum(temperatures) / len(temperatures)
    min_temp = min(temperatures)
    max_temp = max(temperatures)
    return avg_temperature, min_temp, max_temp
def max_wind():
    wind_2024= weather2024.wind_data()
    wind_2023= weather2023.wind_data()
    wind_2022= weather2022.wind_data()
    wind_2021= weather2021.wind_data()
    wind_2020= weather2020.wind_data()
    winds = [wind_2024, wind_2023, wind_2022, wind_2021, wind_2020]
    avg_wind = sum(winds) / len(winds)
    min_wind = min(winds)
    max_wind = max(winds)
#
    return avg_wind, min_wind, max_wind
def sum_precip():
    precipitation_2024= weather2024.precip_data()
    precipitation_2023= weather2023.precip_data()
    precipitation_2022= weather2022.precip_data()
    precipitation_2021= weather2021.precip_data()
    precipitation_2020= weather2020.precip_data()
    precipitations = [precipitation_2024, precipitation_2023, precipitation_2022, precipitation_2021,precipitation_2020]
    avg_precip = sum(precipitations) / len(precipitations)
    min_precip = min(precipitations)
    max_precip = max(precipitations)

    return avg_precip, min_precip, max_precip


weather2024 = Weather(38.8339, -104.8214, 9, 30, 2024)
weather2023 = Weather(38.8339, -104.8214, 9, 30, 2023)
weather2022 = Weather(38.8339, -104.8214, 9, 30, 2022)
weather2021 = Weather(38.8339, -104.8214, 9, 30, 2021)
weather2020 = Weather(38.8339, -104.8214, 9, 30, 2020)


average_temperature, min_temp, max_temp = avg_temp()
avg_wind, min_wind, max_wind = max_wind()
avg_precip, min_precip, max_precip = sum_precip()


print(f"Average Temperature: {average_temperature}")
print(f"Minimum Temperature: {min_temp}")
print(f"Maximum Temperature: {max_temp}")
print(f"Average Wind: {avg_wind}")
print(f"Minimum Wind: {min_wind}")
print(f"Maximum Wind: {max_wind}")
print(f"Average Precip: {avg_precip}")
print(f"Minimum Precip: {min_precip}")
print(f"Maximum Precip: {max_precip}")
# temperature = weather.temp_data()
# wind= weather.wind_data()
# precip= weather.precip_data()
#
# average_temperature, min_temp, max_temp = avg_temp()
# average_wind, min_wind, max_wind = max_wind()
# average_precip, min_precip, max_precip = sum_precip()
#
#
#
# _,max_wind,_ = max_wind(wind)
# print(max_wind)
# # max_temp = max(temperatures)
# min_temp = min(temperatures)
# min_wind = min(wind)
# avg_wind =  sum(wind) / len(wind)
# maximum_wind = max_wind(wind)
# sum_precip = precip_sum(precipitation)
# min_precip = min(precipitation)
# max_precip = max(precipitation)


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
# session.add(entry_2024)
# session.commit()
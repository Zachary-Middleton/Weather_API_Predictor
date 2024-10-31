import weather
from weather import Weather  # Make sure this matches the filename of your Weather class
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker
import sqlalchemy


#methods to pull data from the Weather class for each year
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
    return avg_temperature, min_temp, max_temp, temp_2024, temp_2023, temp_2022, temp_2021, temp_2020
def max_wind():
    wind_2024= weather2024.wind_data()
    wind_2023= weather2023.wind_data()
    wind_2022= weather2022.wind_data()
    wind_2021= weather2021.wind_data()
    wind_2020= weather2020.wind_data()
    winds = [wind_2024, wind_2023, wind_2022, wind_2021, wind_2020]
    avg_wind = sum(winds) / len(winds)
    min_wind = min(winds)
    maximum_wind = max(winds)
#
    return avg_wind, min_wind, maximum_wind, wind_2024, wind_2023, wind_2022, wind_2021, wind_2020
def sum_precip():
    precipitation_2024= weather2024.precip_data()
    precipitation_2023= weather2023.precip_data()
    precipitation_2022= weather2022.precip_data()
    precipitation_2021= weather2021.precip_data()
    precipitation_2020= weather2020.precip_data()
    precipitations = [precipitation_2024, precipitation_2023, precipitation_2022, precipitation_2021,precipitation_2020]
    sum_precips = sum(precipitations)
    avg_precip = sum(precipitations) / len(precipitations)
    min_precip = min(precipitations)
    max_precip = max(precipitations)

    return avg_precip, min_precip, max_precip, sum_precips, precipitation_2024, precipitation_2023, precipitation_2022, precipitation_2021, precipitation_2020

#intializing the Weather class with each year with the latitude, longitude, day, month, and year
weather2024 = Weather(38.8339, -104.8214, 9, 30, 2024)
weather2023 = Weather(38.8339, -104.8214, 9, 30, 2023)
weather2022 = Weather(38.8339, -104.8214, 9, 30, 2022)
weather2021 = Weather(38.8339, -104.8214, 9, 30, 2021)
weather2020 = Weather(38.8339, -104.8214, 9, 30, 2020)

#initializing the variables from the methods above
average_temperature, min_temp, max_temp, temp_2024, temp_2023, temp_2022, temp_2021,temp_2020 = avg_temp()
average_wind, min_wind, maximum_wind, wind_2024, wind_2023, wind_2022, wind_2021, wind_2020 = max_wind()
average_precip, min_precip, max_precip, sum_precips, precipitation_2024, precipitation_2023,precipitation_2022, precipitation_2021, precipitation_2020 = sum_precip()

#base needed to start the SQLAlchemy process of creating a table
Base = sqlalchemy.orm.declarative_base()

#table created for database
class WeatherData(Base):
    __tablename__ = 'weather_data'
    id = Column(Integer, primary_key=True)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    month = Column(Integer, nullable=False)
    day = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    five_year_avg_temp = Column(Float, nullable=True)
    five_year_min_temp = Column(Float, nullable=True)
    five_year_max_temp = Column(Float, nullable=True)
    five_year_avg_wind = Column(Float, nullable=True)
    five_year_min_wind = Column(Float, nullable=True)
    five_year_max_wind = Column(Float, nullable=True)
    five_year_sum_precip = Column(Float, nullable=True)
    five_year_min_precip = Column(Float, nullable=True)
    five_year_max_precip = Column(Float, nullable=True)

    def __init__(self, latitude, longitude, month, day, year,
                 five_year_avg_temp=None, five_year_min_temp=None, five_year_max_temp=None,
                 five_year_avg_wind=None, five_year_min_wind=None, five_year_max_wind=None,
                 five_year_sum_precip=None, five_year_min_precip=None, five_year_max_precip=None):
        self.latitude = latitude
        self.longitude = longitude
        self.month = month
        self.day = day
        self.year = year
        self.five_year_avg_temp = five_year_avg_temp
        self.five_year_min_temp = five_year_min_temp
        self.five_year_max_temp = five_year_max_temp
        self.five_year_avg_wind = five_year_avg_wind
        self.five_year_min_wind = five_year_min_wind
        self.five_year_max_wind = five_year_max_wind
        self.five_year_sum_precip = five_year_sum_precip
        self.five_year_min_precip = five_year_min_precip
        self.five_year_max_precip = five_year_max_precip

    def __repr__(self):
        return (f"{self.id} {self.latitude} {self.longitude} {self.month} {self.day} {self.year} {self.five_year_avg_temp} {self.five_year_min_temp} {self.five_year_max_temp} {self.five_year_avg_wind} {self.five_year_min_wind} {self.five_year_min_wind} {self.five_year_max_wind} {self.five_year_sum_precip} {self.five_year_min_precip} {self.five_year_max_precip}")


#setting up DB type
def setup_database(db_url='sqlite:///weather_data.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # Create all tables in the engine
    Session = sessionmaker(bind=engine)
    return Session()

session = setup_database()

#5 years of entry data
entry_2024 = WeatherData(
    latitude=weather2024.latitude,
    longitude=weather2024.longitude,
    month=9,
    day = 30,
    year = 2024,
    five_year_avg_temp = temp_2024,
    five_year_min_temp =  temp_2024,
    five_year_max_temp = temp_2024,
    five_year_avg_wind = wind_2024,
    five_year_min_wind = wind_2024,
    five_year_max_wind = wind_2024,
    five_year_sum_precip = precipitation_2024,
    five_year_min_precip = precipitation_2024,
    five_year_max_precip = precipitation_2024
)
entry_2023 = WeatherData(
    latitude=weather2023.latitude,
    longitude=weather2023.longitude,
    month=9,
    day = 30,
    year = 2023,
    five_year_avg_temp = temp_2023,
    five_year_min_temp =  temp_2023,
    five_year_max_temp = temp_2023,
    five_year_avg_wind = wind_2023,
    five_year_min_wind = wind_2023,
    five_year_max_wind = wind_2023,
    five_year_sum_precip = precipitation_2023,
    five_year_min_precip = precipitation_2023,
    five_year_max_precip = precipitation_2023
)
entry_2022 = WeatherData(
    latitude=weather2022.latitude,
    longitude=weather2022.longitude,
    month=9,
    day = 30,
    year = 2022,
    five_year_avg_temp = temp_2022,
    five_year_min_temp =  temp_2022,
    five_year_max_temp = temp_2022,
    five_year_avg_wind = wind_2022,
    five_year_min_wind = wind_2022,
    five_year_max_wind = wind_2022,
    five_year_sum_precip = precipitation_2022,
    five_year_min_precip = precipitation_2022,
    five_year_max_precip = precipitation_2022
)
entry_2021 = WeatherData(
    latitude=weather2021.latitude,
    longitude=weather2021.longitude,
    month=9,
    day = 30,
    year = 2021,
    five_year_avg_temp = temp_2021,
    five_year_min_temp =  temp_2021,
    five_year_max_temp = temp_2021,
    five_year_avg_wind = wind_2021,
    five_year_min_wind = wind_2021,
    five_year_max_wind = wind_2021,
    five_year_sum_precip = precipitation_2021,
    five_year_min_precip = precipitation_2021,
    five_year_max_precip = precipitation_2021
)
entry_2020 = WeatherData(
    latitude=weather2020.latitude,
    longitude=weather2020.longitude,
    month=9,
    day = 30,
    year = 2020,
    five_year_avg_temp = temp_2020,
    five_year_min_temp =  temp_2020,
    five_year_max_temp = temp_2020,
    five_year_avg_wind = wind_2020,
    five_year_min_wind = wind_2020,
    five_year_max_wind = wind_2020,
    five_year_sum_precip = precipitation_2020,
    five_year_min_precip = precipitation_2020,
    five_year_max_precip = precipitation_2020
)
#once a variable for each entry year is created, session.add to database
session.add(entry_2024)
session.add(entry_2023)
session.add(entry_2022)
session.add(entry_2021)
session.add(entry_2020)

#last step to confirm data to be added to table
session.commit()
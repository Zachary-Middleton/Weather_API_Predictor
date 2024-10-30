from weather import Weather  # Make sure this matches the filename of your Weather class
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker
import sqlalchemy
#


weather = Weather(38.8339, -104.8214, 9, 30, 2024)
temperature_data = weather.temp_data()
wind_data = weather.wind_data()
precip_data = weather.precip_data()
# print(temperature_data)
def avg_temp(temperature_data):
    average_temp = sum(temperature_data.values()) / len(temperature_data)
    return average_temp
def max_wind(wind_data):
    maximum_wind = max(wind_data.values())
    return maximum_wind
def precip_sum(precip_data):
    precipitation_sum = sum(precip_data.values())
    return precipitation_sum

precipitation_avg = avg_temp(precip_data)
average_temp = avg_temp(temperature_data)
maximum_wind = max_wind(wind_data)


Base = sqlalchemy.orm.declarative_base()

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


def setup_database(db_url='sqlite:///weather_data.db'):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)  # Create all tables in the engine
    Session = sessionmaker(bind=engine)
    return Session()

session = setup_database()







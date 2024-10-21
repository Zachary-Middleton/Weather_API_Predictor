from weather import Weather  # Make sure this matches the filename of your Weather class
from sqlalchemy import create_engine, Column, Float, Integer
from sqlalchemy.orm import sessionmaker
import sqlalchemy


# def main():
#     # Create an instance of the Weather class
#     weather = Weather(38.8339, -104.8214, 9, 30, 2024)
#
#     # Call methods to get the average temperature, wind speed, and precipitation
#     avg_temp = weather.temp_data()
#     max_wind = weather.wind_data()
#     avg_precip = weather.precip_data()
#
#     # Print the results
#     print(f"5-Year Average Temperature: {avg_temp:.2f}°F")
#     print(f"5-Year Max Wind Speed: {max_wind:.2f} mph")
#     print(f"5-Year Total Precipitation: {avg_precip:.2f} inches")\
#
# if __name__ == "__main__":
#     main()
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

    def __init__(self):
        self.id = id
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
        self.five_year_max_temp = five_year_max_temp
        self.five_year_max_temp = five_year_max_temp
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

# session = Session()
# weather_data_entry = Weather(
#         latitude=Weather(latitude)
#         longitude=Weather.longitude,
#         month=Weather(month),
#         day=Weather(day),
#         year=Weather(year),
#         five_year_avg_temp=avg_temp,
#         five_year_max_wind=max_wind,
#         five_year_sum_precip=avg_precip,
#         # Set other fields to None or appropriate values as needed
#     )






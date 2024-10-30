
from weather import Weather
import unittest


class TestWeather(unittest.TestCase):

    def test_initial_latitude(self):
        # Create an instance of the Weather class
        weather_latitude = Weather(38.8339, -104.8214, 9, 30, 2024)

        # Assert that the latitude is set correctly
        self.assertEqual(weather_latitude.latitude, 38.8339)

    def test_initial_longitude(self):
        weather_longitude = Weather(38.8339, -104.8214, 9, 30, 2024)

        # Assert that the longitude is set correctly
        self.assertEqual(weather_longitude.longitude, -104.8214)

    def test_day(self):
        weather_day = Weather(38.8339, -104.8214, 9, 30, 2024)

        # Assert that the longitude is set correctly
        self.assertEqual(weather_day.day, 30)



if __name__ == '__main__':
    unittest.main()


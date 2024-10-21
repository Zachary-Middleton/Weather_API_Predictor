
from weather import Weather
import unittest


class TestWeather(unittest.TestCase):

    def test_initial_latitude(self):
        # Create an instance of the Weather class
        weather_latidude = Weather(38.8339, -104.8214, 9, 30, 2024)

        # Assert that the latitude is set correctly
        self.assertEqual(weather_latidude.latitude, 38.8339)

    def test_initial_longitude(self):
        weather_longitude = Weather(38.8339, -104.8214, 9, 30, 2024)
        self.assertEqual(weather_longitude.longitude, -104.8214)

    def test_five_year_avg_temp(self):
        weather_temp = Weather(38.8339, -104.8214, 9, 30, 2024)
        weather_temp.temp_data()  # Call the method to calculate average temperature
        self.assertAlmostEqual(weather_temp.five_year_avg_temp, 62.78)  # Compare the attribute, not the object


if __name__ == '__main__':
    unittest.main()


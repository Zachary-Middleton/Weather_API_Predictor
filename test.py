
from weather import Weather
import unittest

class Test_weather(unittest.TestCase):
    def test_max_temp(self):
        self.assertEqual(five_year_avg_temp, 62.78)
    def test_max_wind(self):
        self.assertEqual(five_year_max_wind, 18.60)
    def test_sum_precip(self):
        self.assertEqual(five_year_sum_precip, 0.09)

if __name__ == '__main__':
    unittest.main()


import unittest

from weather_info.infrastructure.open_weather_map.OpenWeatherMapClient import client


class MyTestCase(unittest.TestCase):
    @unittest.SkipTest
    def test_get_weather(self):
        res = client.get_weather_for_coordinates(latitude=45.75, longitude=4.85)
        self.assertIsNotNone(res)

    @unittest.SkipTest
    def test_get_forecast(self):
        res = client.get_forecast_for_coordinates(latitude=45.75, longitude=4.85)
        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()

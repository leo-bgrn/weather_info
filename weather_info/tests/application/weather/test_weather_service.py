import unittest
from unittest.mock import patch, Mock

from weather_info.application.weather import WeatherService


class MyTestCase(unittest.TestCase):
    @patch("weather_info.application.weather.WeatherService.LocationProvider")
    @patch("weather_info.application.weather.WeatherService.WeatherProvider")
    def test_get_weather(self, weather_location_mocked, location_provider_mocked):
        location_provider_mocked.get_location.return_value = None
        res = WeatherService.get_weather("test")

        self.assertIsNone(res)
        location_provider_mocked.get_location.assert_called_once_with("test")
        self.assertFalse(weather_location_mocked.get_weather.called)

    @patch("weather_info.application.weather.WeatherService.LocationProvider")
    @patch("weather_info.application.weather.WeatherService.WeatherProvider")
    def test_get_weather(self, weather_location_mocked, location_provider_mocked):
        location_provider_mocked.get_location.return_value = Mock()
        weather_location_mocked.get_weather.return_value = Mock()
        res = WeatherService.get_weather("test")

        self.assertEqual(weather_location_mocked.get_weather.return_value, res)
        location_provider_mocked.get_location.assert_called_once_with("test")
        weather_location_mocked.get_weather.assert_called_once_with(location_provider_mocked.get_location.return_value)



if __name__ == '__main__':
    unittest.main()

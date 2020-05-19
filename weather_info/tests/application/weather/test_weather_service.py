import unittest
from unittest.mock import patch, Mock

from weather_info.application.weather import WeatherService


class MyTestCase(unittest.TestCase):
    @patch("weather_info.application.weather.WeatherService.LocationProvider")
    @patch("weather_info.application.weather.WeatherService.WeatherProvider")
    def test_get_weather_with_None(self, weather_location_mocked, location_provider_mocked):
        location_provider_mocked.get_location.return_value = None
        res = WeatherService.get_weather("test")

        self.assertIsNone(res)
        location_provider_mocked.get_location.assert_called_once_with("test")
        self.assertFalse(weather_location_mocked.get_weather.called)

    @patch("weather_info.application.weather.WeatherService.LocationProvider")
    @patch("weather_info.application.weather.WeatherService.WeatherProvider")
    @patch("weather_info.application.weather.WeatherService.WindDesignationComputer")
    def test_get_weather(self, wind_designation_mocked, weather_location_mocked, location_provider_mocked):
        location_provider_mocked.get_location.return_value = Mock()
        weather_location_mocked.get_weather.return_value = Mock()
        wind_designation_mocked.compute_wind_designation.return_value = "wind_designation"
        res = WeatherService.get_weather("test")

        self.assertEqual("wind_designation", res.wind.designation)
        location_provider_mocked.get_location.assert_called_once_with("test")
        weather_location_mocked.get_weather.assert_called_once_with(location_provider_mocked.get_location.return_value)


if __name__ == '__main__':
    unittest.main()

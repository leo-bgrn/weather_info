import unittest
from unittest.mock import patch, Mock

from weather_info.domain.location.Coordinates import Coordinates
from weather_info.domain.location.Location import Location
from weather_info.domain.weather import WeatherProvider


class MyTestCase(unittest.TestCase):
    @patch("weather_info.domain.weather.WeatherProvider.OpenWeatherMapService")
    def test_get_weather(self, service_mocked):
        service_mocked.get_weather_from_location.return_value = Mock()

        location = Location(coordinates=Coordinates(latitude=45.76, longitude=4.83),
                            label="Lyon, France", country="France")

        res = WeatherProvider.get_weather(location)

        self.assertEqual(service_mocked.get_weather_from_location.return_value, res)
        service_mocked.get_weather_from_location.assert_called_once_with(location)


if __name__ == '__main__':
    unittest.main()

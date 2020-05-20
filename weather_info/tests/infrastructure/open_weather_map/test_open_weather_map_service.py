import unittest
from unittest.mock import patch

from weather_info.domain.location.CardinalPoint import CardinalPoint
from weather_info.domain.location.Coordinates import Coordinates
from weather_info.domain.location.Location import Location
from weather_info.infrastructure.open_weather_map import OpenWeatherMapService


class MyTestCase(unittest.TestCase):
    @patch("weather_info.infrastructure.open_weather_map.OpenWeatherMapService.client")
    def test_get_forecast_from_location(self, client_mocked):
        return_from_client = {
            "lat": 45.76,
            "lon": 4.83,
            "timezone": "Europe/Paris",
            "timezone_offset": 7200,
            "daily": [
                {
                    "dt": 1589972400,
                    "sunrise": 1589947423,
                    "sunset": 1590001861,
                    "temp": {
                        "day": 26.24,
                        "min": 17.52,
                        "max": 26.24,
                        "night": 17.52,
                        "eve": 24.43,
                        "morn": 26.24
                    },
                    "feels_like": {
                        "day": 21.76,
                        "night": 16.79,
                        "eve": 21.62,
                        "morn": 21.76
                    },
                    "pressure": 1015,
                    "humidity": 42,
                    "dew_point": 12.32,
                    "wind_speed": 7.42,
                    "wind_deg": 345,
                    "weather": [
                        {
                            "id": 800,
                            "main": "Clear",
                            "description": "clear sky",
                            "icon": "01d"
                        }
                    ],
                    "clouds": 0,
                    "uvi": 7.73
                }
            ]
        }
        client_mocked.get_forecast_for_coordinates.return_value = return_from_client

        location = Location(coordinates=Coordinates(latitude=45.76, longitude=4.83),
                            label="Lyon, France", country="France")

        res = OpenWeatherMapService.get_forecast_from_location(location)

        client_mocked.get_forecast_for_coordinates.assert_called_once_with(latitude=location.coordinates.latitude,
                                                                          longitude=location.coordinates.longitude)

        self.assertEqual(1, len(res.forecast))
        self.assertEqual(return_from_client["daily"][0]["weather"][0]["main"], res.forecast[0].main)
        self.assertEqual(return_from_client["daily"][0]["weather"][0]["description"], res.forecast[0].description)
        self.assertEqual(CardinalPoint.NORTH, res.forecast[0].wind.cardinal_point)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import patch

from weather_info.domain.location.CardinalPoint import CardinalPoint
from weather_info.domain.location.Coordinates import Coordinates
from weather_info.domain.location.Location import Location
from weather_info.infrastructure.open_weather_map import OpenWeatherMapService


class MyTestCase(unittest.TestCase):
    @patch("weather_info.infrastructure.open_weather_map.OpenWeatherMapService.client")
    def test_get_weather_from_location(self, client_mocked):
        return_from_client = {
            "coord": {
                "lon": 4.83,
                "lat": 45.76
            },
            "weather": [
                {
                    "id": 804,
                    "main": "Clouds",
                    "description": "overcast clouds",
                    "icon": "04d"
                }
            ],
            "base": "stations",
            "main": {
                "temp": 10.01,
                "feels_like": 4.25,
                "temp_min": 8.89,
                "temp_max": 11,
                "pressure": 1005,
                "humidity": 81
            },
            "visibility": 10000,
            "wind": {
                "speed": 7.2,
                "deg": 350
            },
            "clouds": {
                "all": 90
            },
            "dt": 1589217489,
            "sys": {
                "type": 1,
                "id": 6505,
                "country": "FR",
                "sunrise": 1589170429,
                "sunset": 1589223622
            },
            "timezone": 7200,
            "id": 8015556,
            "name": "Vieux Lyon",
            "cod": 200
        }
        client_mocked.get_weather_for_coordinates.return_value = return_from_client

        location = Location(coordinates=Coordinates(latitude=45.76, longitude=4.83),
                            label="Lyon, France", country="France")

        res = OpenWeatherMapService.get_weather_from_location(location)

        client_mocked.get_weather_for_coordinates.assert_called_once_with(latitude=location.coordinates.latitude,
                                                                          longitude=location.coordinates.longitude)

        self.assertEqual(return_from_client["weather"][0]["main"], res.main)
        self.assertEqual(return_from_client["weather"][0]["description"], res.description)
        self.assertEqual(return_from_client["main"]["temp"], res.temperature.main)
        self.assertEqual(CardinalPoint.NORTH, res.wind.cardinal_point)


if __name__ == '__main__':
    unittest.main()

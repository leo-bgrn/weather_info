import unittest
from datetime import date
from unittest.mock import patch

from weather_info.domain.location.Coordinates import Coordinates
from weather_info.domain.location.Location import Location
from weather_info.domain.pollution.Pollution import Pollution
from weather_info.infrastructure.air_visual import AirVisualService


class MyTestCase(unittest.TestCase):
    @patch("weather_info.infrastructure.air_visual.AirVisualService.client")
    def test_get_pollution_level_from_location(self, client_mocked):
        client_mocked.get_data_from_lat_lng.return_value = {
            "status": "success",
            "data": {
                "city": "La Mulatiere",
                "state": "Auvergne-Rhone-Alpes",
                "country": "France",
                "location": {
                    "type": "Point",
                    "coordinates": [
                        4.81816,
                        45.72008
                    ]
                },
                "current": {
                    "weather": {
                        "ts": "2020-05-20T17:00:00.000Z",
                        "tp": 25,
                        "pr": 1015,
                        "hu": 42,
                        "ws": 8.2,
                        "wd": 350,
                        "ic": "01d"
                    },
                    "pollution": {
                        "ts": "2020-05-20T16:00:00.000Z",
                        "aqius": 63,
                        "mainus": "p2",
                        "aqicn": 34,
                        "maincn": "p1"
                    }
                }
            }
        }

        location = Location(coordinates=Coordinates(latitude=45.76, longitude=4.83),
                            label="Lyon, France", country="France")
        res = AirVisualService.get_pollution_level_from_location(location)

        expected_res = Pollution(date(2020, 5, 20), location, 63)
        self.assertEqual(expected_res, res)
        client_mocked.get_data_from_lat_lng.assert_called_once_with(
            latitude=location.coordinates.latitude, longitude=location.coordinates.longitude
        )


if __name__ == '__main__':
    unittest.main()

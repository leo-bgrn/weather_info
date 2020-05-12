import unittest
from unittest import TestCase
from unittest.mock import patch

from weather_info.infrastructure.open_cage_data import OpenCageDataService


class TestOpenCageDataService(TestCase):
    @unittest.SkipTest
    def test_search_location_it(self):
        res = OpenCageDataService.search_location("Lyon France")

        self.assertIsNotNone(res)

    @patch("weather_info.infrastructure.open_cage_data.open_cage_data_service.client")
    def test_search_location(self, client_mocked):
        client_mocked.forward_search.return_value = {
            "results": [{
                "formatted": "Lyon, France",
                "geometry": {
                    "lat": 0.0,
                    "lng": 1.0
                },
                "components": {
                    "country": "France"
                }
            }]
        }
        res = OpenCageDataService.search_location("Lyon, France")

        self.assertIsNotNone(res)
        self.assertEqual("Lyon, France", res.label)
        self.assertEqual(0.0, res.coordinates.latitude)
        self.assertEqual(1.0, res.coordinates.longitude)
        self.assertEqual("France", res.country)


if __name__ == '__main__':
    unittest.main()

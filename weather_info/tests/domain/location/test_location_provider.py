import unittest
from unittest.mock import patch, Mock

from weather_info.domain.location import LocationProvider


class MyTestCase(unittest.TestCase):
    @patch("weather_info.domain.location.LocationProvider.open_cage_data_service")
    def test_get_location(self, service_mocked):
        service_mocked.search_location.return_value = Mock()

        res = LocationProvider.get_location("test")

        self.assertEqual(service_mocked.search_location.return_value, res)
        service_mocked.search_location.assert_called_once_with("test")


if __name__ == '__main__':
    unittest.main()

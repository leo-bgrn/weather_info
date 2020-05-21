import unittest

from weather_info.infrastructure.air_visual.AirVisualClient import client


class MyTestCase(unittest.TestCase):
    @unittest.SkipTest
    def test_get_data_from_lat_lng(self):
        res = client.get_data_from_lat_lng(45.7, 4.83)

        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest import TestCase

from weather_info import create_app
from weather_info.infrastructure.open_cage_data.open_cage_data_client import OpenCageDataClient

app = create_app("test")


class TestOpenCageDataClient(TestCase):
    @unittest.SkipTest
    def test_forward_search(self):
        with app.app_context():
            client = OpenCageDataClient()
        res = client.forward_search("Lyon, France")

        self.assertIsNotNone(res)


if __name__ == '__main__':
    unittest.main()

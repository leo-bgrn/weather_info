import logging

import requests

from weather_info.core.exceptions import AirVisualException
from weather_info.core.logger import console_handler
from weather_info.params.params import actual_config

logger = logging.getLogger("air_visual")
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


class AirVisualClient:
    def __init__(self):
        self.url = actual_config["AIR_VISUAL"]["url"]
        self.api_key = actual_config["AIR_VISUAL"]["api_key"]
        logger.info("Starting OpenCageDataClient...")

    def get_data_from_lat_lng(self, latitude: float, longitude: float):
        url = self.url + "/nearest_city"

        params = {
            "lat": latitude,
            "lon": longitude,
            "key": self.api_key
        }

        logger.debug(f"--> GET {url}")
        response = requests.get(url=url, params=params, verify=False)

        if response.ok:
            res = response.json()
            logger.debug(f"GET <-- {url} - response: {res}")
            return res
        else:
            logger.error(f"GET <-- {url} - {response.status_code} - {response.text}")
            raise AirVisualException(
                f"An error occurred with the AirVisual API. Error: {response.status_code} - {response.text}")


client = AirVisualClient()

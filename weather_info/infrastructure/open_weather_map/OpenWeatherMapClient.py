import logging

import requests

from weather_info.core.exceptions import OpenWeatherMapException
from weather_info.core.logger import console_handler
from weather_info.params.params import actual_config

logger = logging.getLogger("open_weather_map")
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


class OpenWeatherMapClient:
    def __init__(self):
        self.url = actual_config["OPEN_WEATHER_MAP"]["url"]
        self.api_key = actual_config["OPEN_WEATHER_MAP"]["api_key"]
        logger.info("Starting OpenWeatherMapClient...")

    def get_weather_for_coordinates(self, latitude: float, longitude: float):
        url = f"{self.url}/weather"

        query_params = {
            "lat": latitude,
            "lon": longitude,
            "units": "metric",
            "appid": self.api_key
        }

        logger.debug(f"GET --> {url}")
        response = requests.get(url=url, params=query_params)

        if response.ok:
            res = response.json()
            logger.debug(f"GET <-- {url} - response: {res}")
            return res

        else:
            logger.error(f"GET <-- {url} - {response.status_code} - {response.text}")
            raise OpenWeatherMapException(
                f"An error occurred with the OpenWeatherMap API. Error: {response.status_code} - {response.text}")


client = OpenWeatherMapClient()

import logging

import requests

from weather_info.core.exceptions import OpenCageDataException
from weather_info.core.logger import console_handler
from weather_info.params.params import actual_config

logger = logging.getLogger("open_cage_data")
logger.setLevel(logging.DEBUG)
logger.addHandler(console_handler)


class OpenCageDataClient:
    def __init__(self):
        self.url = actual_config["OPEN_CAGE_DATA"]["url"]
        self.api_key = actual_config["OPEN_CAGE_DATA"]["api_key"]
        logger.info("Starting OpenCageDataClient...")

    def forward_search(self, query: str) -> dict:
        query_split_by_space = query.split(" ")
        query_joined_by_plus = "+".join(query_split_by_space)

        url = f"{self.url}?q={query_joined_by_plus}&limit=1&key={self.api_key}"

        logger.debug(f"GET --> {url}")
        response = requests.get(url)

        if response.ok:
            res = response.json()
            logger.debug(f"GET <-- {url} - response: {res}")
            return res
        else:
            logger.error(f"GET <-- {url} - {response.status_code} - {response.text}")
            raise OpenCageDataException(
                f"An error occurred with the OpenCageData API. Error: {response.status_code} - {response.text}")


client = OpenCageDataClient()

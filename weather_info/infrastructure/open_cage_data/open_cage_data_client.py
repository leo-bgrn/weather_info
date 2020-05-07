import logging

import requests
from flask import current_app, app

from weather_info.core.exceptions import OpenCageDataException
from weather_info.core.logger import console_handler

logger = logging.getLogger("open_cage_data")

logger.addHandler(console_handler)


class OpenCageDataClient:
    def __init__(self):
        self.url = current_app.config["OPEN_CAGE_DATA"]["url"]
        self.api_key = current_app.config["OPEN_CAGE_DATA"]["api_key"]

    def forward_search(self, query: str):
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

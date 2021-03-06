from copy import deepcopy
from typing import List

from weather_info.params.secrets_loader import open_cage_data_api_key, open_weather_map_api_key, air_visual_api_key

basic = {
    "CONFIG_NAME": "base",
    "OPEN_CAGE_DATA": {
        "url": "https://api.opencagedata.com/geocode/v1/json",
        "api_key": open_cage_data_api_key
    },
    "OPEN_WEATHER_MAP": {
        "url": "https://api.openweathermap.org/data/2.5",
        "api_key": open_weather_map_api_key
    },
    "AIR_VISUAL": {
        "url": "https://api.airvisual.com/v2",
        "api_key": air_visual_api_key
    }
}

dev = deepcopy(basic)
dev["CONFIG_NAME"] = "dev"

test = deepcopy(basic)
test["CONFIG_NAME"] = "test"

EXPORT_CONFIGS: [List[dict]] = [dev, test]
config_by_name = {cfg["CONFIG_NAME"]: cfg for cfg in EXPORT_CONFIGS}

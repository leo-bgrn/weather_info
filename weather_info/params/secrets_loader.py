import os

open_cage_data_api_key = None
open_weather_map_api_key = None
air_visual_api_key = None

if os.path.exists("./secret_config.py"):
    from weather_info.params.secret_config import open_cage_data_api_key as ocd_key
    from weather_info.params.secret_config import open_weather_map_api_key as owm_key
    from weather_info.params.secret_config import air_visual_api_key as ac_key

    open_cage_data_api_key = ocd_key
    open_weather_map_api_key = owm_key
    air_visual_api_key = ac_key
else:
    if "OPEN_CAGE_DATA_API_KEY" in os.environ:
        open_cage_data_api_key = os.environ["OPEN_CAGE_DATA_API_KEY"]
    if "OPEN_WEATHER_MAP_API_KEY" in os.environ:
        open_weather_map_api_key = os.environ["OPEN_WEATHER_MAP_API_KEY"]
    if "AIR_VISUAL_API_KEY" in os.environ:
        air_visual_api_key = os.environ["AIR_VISUAL_API_KEY"]

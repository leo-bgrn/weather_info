import os

from weather_info.params.configs import config_by_name

if "FLASK_ENV" in os.environ:
    actual_config = config_by_name[os.environ["FLASK_ENV"].lower()]
else:
    actual_config = config_by_name["test"]

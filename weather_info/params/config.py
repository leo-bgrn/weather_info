from typing import List, Type
from weather_info.params.secret_config import open_cage_data_api_key


class BaseConfig:
    CONFIG_NAME = "base"
    DEBUG = False
    OPEN_CAGE_DATA = {
        "url": "https://api.opencagedata.com/geocode/v1/json",
        "api_key": open_cage_data_api_key
    }


class DevelopmentConfig(BaseConfig):
    CONFIG_NAME = "dev"
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    CONFIG_NAME = "test"
    DEBUG = True
    TESTING = True


EXPORT_CONFIGS: List[Type[BaseConfig]] = [
    DevelopmentConfig,
    TestingConfig
]
config_by_name = {cfg.CONFIG_NAME: cfg for cfg in EXPORT_CONFIGS}

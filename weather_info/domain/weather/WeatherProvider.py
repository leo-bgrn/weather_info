from weather_info.domain.location.Location import Location
from weather_info.domain.forecast.Weather import Weather
from weather_info.infrastructure.open_weather_map import OpenWeatherMapService


def get_weather(location: Location) -> Weather:
    return OpenWeatherMapService.get_weather_from_location(location)


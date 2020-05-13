from typing import Optional

from weather_info.domain.location import LocationProvider
from weather_info.domain.location.Location import Location
from weather_info.domain.weather import WeatherProvider
from weather_info.domain.weather.Weather import Weather


def get_weather(geographical_label: str) -> Optional[Weather]:
    location: Optional[Location] = LocationProvider.get_location(geographical_label)

    if location is None:
        return None

    weather: Weather = WeatherProvider.get_weather(location)

    return weather

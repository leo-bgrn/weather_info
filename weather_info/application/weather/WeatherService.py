from typing import Optional

from weather_info.application.weather.WeatherView import WeatherView
from weather_info.application.weather.WindView import WindView
from weather_info.domain.location import LocationProvider
from weather_info.domain.location.Location import Location
from weather_info.domain.weather import WeatherProvider
from weather_info.domain.weather.Weather import Weather
from weather_info.domain.wind import WindDesignationComputer


def get_weather(geographical_label: str) -> Optional[WeatherView]:
    location: Optional[Location] = LocationProvider.get_location(geographical_label)

    if location is None:
        return None

    weather: Weather = WeatherProvider.get_weather(location)

    wind_designation: str = WindDesignationComputer.compute_wind_designation(weather.wind)
    weather_view: WeatherView = WeatherView(
        location=weather.location,
        main=weather.main,
        description=weather.description,
        temperature=weather.temperature,
        wind=WindView(weather.wind, wind_designation),
        cloudiness=weather.cloudiness,
        humidity=weather.humidity
    )

    return weather_view

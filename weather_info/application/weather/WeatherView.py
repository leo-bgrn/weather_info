from dataclasses import dataclass

from weather_info.application.weather.WindView import WindView
from weather_info.domain.location.Location import Location
from weather_info.domain.weather.Temperature import Temperature


@dataclass
class WeatherView:
    location: Location
    main: str
    description: str
    temperature: Temperature
    wind: WindView
    cloudiness: float
    humidity: float
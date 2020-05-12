from dataclasses import dataclass

from weather_info.domain.location.Location import Location
from weather_info.domain.weather.Temperature import Temperature
from weather_info.domain.weather.Wind import Wind


@dataclass
class Weather:
    location: Location
    main: str
    description: str
    temperature: Temperature
    wind: Wind
    cloudiness: float
    humidity: float

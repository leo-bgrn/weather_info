from dataclasses import dataclass
from datetime import date

from weather_info.domain.forecast.Temperature import Temperature
from weather_info.domain.wind.Wind import Wind


@dataclass
class Weather:
    value_date: date
    main: str
    description: str
    temperature: Temperature
    wind: Wind
    cloudiness: float
    humidity: float
    uv_index: float

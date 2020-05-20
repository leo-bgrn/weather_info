from dataclasses import dataclass
from datetime import date

from weather_info.application.forecast.WindView import WindView
from weather_info.domain.forecast.Temperature import Temperature


@dataclass
class WeatherView:
    value_date: date
    main: str
    description: str
    temperature: Temperature
    wind: WindView
    cloudiness: float
    humidity: float

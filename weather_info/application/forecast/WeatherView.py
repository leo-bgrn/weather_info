from dataclasses import dataclass
from datetime import date
from typing import Optional

from weather_info.application.forecast.PollutionView import PollutionView
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
    pollution: Optional[PollutionView]

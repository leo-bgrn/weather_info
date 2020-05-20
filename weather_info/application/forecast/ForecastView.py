from dataclasses import dataclass
from typing import List

from weather_info.application.forecast.WeatherView import WeatherView
from weather_info.domain.location.Location import Location


@dataclass
class ForecastView:
    forecast: List[WeatherView]
    location: Location

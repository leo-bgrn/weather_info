from dataclasses import dataclass
from typing import List

from weather_info.domain.forecast.Weather import Weather
from weather_info.domain.location.Location import Location


@dataclass
class Forecast:
    forecast: List[Weather]
    location: Location

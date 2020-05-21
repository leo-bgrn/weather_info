from dataclasses import dataclass
from datetime import date

from weather_info.domain.location.Location import Location


@dataclass
class Pollution:
    value_date: date
    location: Location
    air_quality_level_aqius: int

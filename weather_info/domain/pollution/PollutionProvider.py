from typing import Optional

from weather_info.domain.location.Location import Location
from weather_info.domain.pollution.Pollution import Pollution
from weather_info.infrastructure.air_visual import AirVisualService


def get_pollution(location: Location) -> Optional[Pollution]:
    return AirVisualService.get_pollution_level_from_location(location)

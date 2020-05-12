from typing import Optional

from weather_info.domain.location.Location import Location
from weather_info.infrastructure.open_cage_data import OpenCageDataService


def get_location(query: str) -> Optional[Location]:
    return OpenCageDataService.search_location(query)

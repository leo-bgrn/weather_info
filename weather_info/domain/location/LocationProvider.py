from typing import Optional

from weather_info.domain.location.Location import Location
from weather_info.infrastructure.open_cage_data import open_cage_data_service


def get_location(query: str) -> Optional[Location]:
    return open_cage_data_service.search_location(query)

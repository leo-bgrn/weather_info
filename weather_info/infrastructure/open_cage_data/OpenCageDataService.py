from typing import Optional

from weather_info.domain.location.Coordinates import Coordinates
from weather_info.domain.location.Location import Location
from weather_info.infrastructure.open_cage_data.OpenCageDataClient import client


def search_location(label: str) -> Optional[Location]:
    response = client.forward_search(label)

    if len(response["results"]) < 1:
        return None

    result = response["results"][0]

    return Location(
        coordinates=Coordinates(latitude=result["geometry"]["lat"], longitude=result["geometry"]["lng"]),
        label=result["formatted"],
        country=result["components"]["country"]
    )

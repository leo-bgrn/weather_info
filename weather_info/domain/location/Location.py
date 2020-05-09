from dataclasses import dataclass

from weather_info.domain.location.Coordinates import Coordinates


@dataclass
class Location:
    coordinates: Coordinates
    label: str
    country: str

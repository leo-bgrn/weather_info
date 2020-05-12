from dataclasses import dataclass

from weather_info.domain.location.CardinalPoint import CardinalPoint


@dataclass
class Wind:
    speed: float
    cardinal_point: CardinalPoint
    unit: str = "meter/sec"

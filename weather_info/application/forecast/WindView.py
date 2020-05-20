from dataclasses import dataclass

from weather_info.domain.location.CardinalPoint import CardinalPoint
from weather_info.domain.wind import WindDesignationComputer
from weather_info.domain.wind.Wind import Wind


@dataclass(init=False)
class WindView:
    speed: float
    cardinal_point: CardinalPoint
    unit: str
    designation: str

    def __init__(self, wind: Wind, wind_designation: str):
        self.speed = wind.speed
        self.cardinal_point = wind.cardinal_point
        self.unit = wind.unit
        self.designation = wind_designation

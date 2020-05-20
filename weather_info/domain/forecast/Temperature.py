from dataclasses import dataclass


@dataclass
class TemperatureData:
    temp: int
    feels_like: int


@dataclass
class Temperature:
    min: int
    max: int
    morning: TemperatureData
    day: TemperatureData
    evening: TemperatureData
    night: TemperatureData
    unit: str = "Celsius"

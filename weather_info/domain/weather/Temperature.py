from dataclasses import dataclass


@dataclass
class Temperature:
    main: int
    feels_like: int
    min: int
    max: int
    unit: str = "Celsius"

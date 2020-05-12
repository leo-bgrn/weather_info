from enum import Enum


class CardinalPoint(Enum):
    NORTH = "NORTH"
    NORTH_EAST = "NORTH-EAST"
    EAST = "EAST"
    SOUTH_EAST = "SOUTH-EAST"
    SOUTH = "SOUTH"
    SOUTH_WEST = "SOUTH-WEST"
    WEST = "WEST"
    NORTH_WEST = "NORTH-WEST"

    @classmethod
    def of(cls, degrees: float):
        if degrees < 0 or degrees > 360:
            raise ValueError("Cardinal Point should be in 0° and 360°")
        if degrees < 22.5 or degrees > 337.5:
            return cls.NORTH
        elif degrees < 67.5:
            return cls.NORTH_EAST
        elif degrees < 112.5:
            return cls.EAST
        elif degrees < 157.5:
            return cls.SOUTH_EAST
        elif degrees < 202.5:
            return cls.SOUTH
        elif degrees < 247.5:
            return cls.SOUTH_WEST
        elif degrees < 292.5:
            return cls.WEST
        elif degrees < 337.5:
            return cls.NORTH_WEST

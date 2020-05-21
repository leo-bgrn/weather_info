from dataclasses import dataclass


@dataclass
class PollutionView:
    air_quality_level_aqius: int
    air_quality_level_of_concern: str
    air_quality_description: str

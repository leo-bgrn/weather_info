from datetime import datetime
from typing import Optional

from weather_info.domain.location.Location import Location
from weather_info.domain.pollution.Pollution import Pollution
from weather_info.infrastructure.air_visual.AirVisualClient import client


def get_pollution_level_from_location(location: Location) -> Optional[Pollution]:
    response = client.get_data_from_lat_lng(latitude=location.coordinates.latitude,
                                            longitude=location.coordinates.longitude)

    if "status" in response and response["status"] == "success":
        if "data" in response and "current" in response["data"] and "pollution" in response["data"]["current"]:
            if "aqius" in response["data"]["current"]["pollution"] and "ts" in response["data"]["current"]["pollution"]:
                return Pollution(
                    value_date=datetime.strptime(response["data"]["current"]["pollution"]["ts"][:10],
                                                 "%Y-%m-%d").date(),
                    air_quality_level_aqius=response["data"]["current"]["pollution"]["aqius"],
                    location=location
                )

    return None

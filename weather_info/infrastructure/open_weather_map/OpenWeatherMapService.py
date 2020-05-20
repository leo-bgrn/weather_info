from datetime import datetime
from typing import List

from weather_info.domain.forecast.Forecast import Forecast
from weather_info.domain.forecast.Temperature import Temperature, TemperatureData
from weather_info.domain.forecast.Weather import Weather
from weather_info.domain.location.CardinalPoint import CardinalPoint
from weather_info.domain.location.Location import Location
from weather_info.domain.wind.Wind import Wind
from weather_info.infrastructure.open_weather_map.OpenWeatherMapClient import client


def get_forecast_from_location(location: Location) -> Forecast:
    response = client.get_forecast_for_coordinates(latitude=location.coordinates.latitude,
                                                   longitude=location.coordinates.longitude)

    res: List[Weather] = []

    for forecast in response["daily"]:
        res.append(Weather(
            value_date=datetime.fromtimestamp(forecast["dt"]).date(),
            main=forecast["weather"][0]["main"],
            description=forecast["weather"][0]["description"],
            temperature=Temperature(
                min=int(forecast["temp"]["min"]),
                max=int(forecast["temp"]["max"]),
                morning=TemperatureData(
                    temp=int(forecast["temp"]["morn"]),
                    feels_like=int(forecast["feels_like"]["morn"])
                ),
                day=TemperatureData(
                    temp=int(forecast["temp"]["day"]),
                    feels_like=int(forecast["feels_like"]["day"])
                ),
                evening=TemperatureData(
                    temp=int(forecast["temp"]["eve"]),
                    feels_like=int(forecast["feels_like"]["eve"])
                ),
                night=TemperatureData(
                    temp=int(forecast["temp"]["night"]),
                    feels_like=int(forecast["feels_like"]["night"])
                )
            ),
            wind=Wind(
                speed=forecast["wind_speed"],
                cardinal_point=CardinalPoint.of(forecast["wind_deg"])
            ),
            cloudiness=forecast["clouds"],
            humidity=forecast["humidity"],
            uv_index=forecast["uvi"]
        ))

    return Forecast(forecast=res, location=location)

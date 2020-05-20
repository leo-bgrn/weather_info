from typing import Optional, List

from weather_info.application.forecast.ForecastView import ForecastView
from weather_info.application.forecast.WeatherView import WeatherView
from weather_info.application.forecast.WindView import WindView
from weather_info.domain.forecast import ForecastProvider
from weather_info.domain.forecast.Forecast import Forecast
from weather_info.domain.location import LocationProvider
from weather_info.domain.location.Location import Location
from weather_info.domain.wind import WindDesignationComputer


def get_forecast(geographical_label: str) -> Optional[ForecastView]:
    location: Optional[Location] = LocationProvider.get_location(geographical_label)

    if location is None:
        return None

    forecast: Forecast = ForecastProvider.get_forecast(location)

    res: List[WeatherView] = []

    for weather in forecast.forecast:
        wind_designation: str = WindDesignationComputer.compute_wind_designation(weather.wind)
        res.append(WeatherView(
            value_date=weather.value_date,
            main=weather.main,
            description=weather.description,
            temperature=weather.temperature,
            wind=WindView(weather.wind, wind_designation),
            cloudiness=weather.cloudiness,
            humidity=weather.humidity
        ))

    return ForecastView(forecast=res, location=location)

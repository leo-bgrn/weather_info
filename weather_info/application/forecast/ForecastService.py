from typing import Optional, List

from weather_info.application.forecast import PollutionViewFactory
from weather_info.application.forecast.ForecastView import ForecastView
from weather_info.application.forecast.PollutionView import PollutionView
from weather_info.application.forecast.WeatherView import WeatherView
from weather_info.application.forecast.WindView import WindView
from weather_info.domain.forecast import ForecastProvider
from weather_info.domain.forecast.Forecast import Forecast
from weather_info.domain.location import LocationProvider
from weather_info.domain.location.Location import Location
from weather_info.domain.pollution import PollutionProvider
from weather_info.domain.pollution.Pollution import Pollution
from weather_info.domain.wind import WindDesignationComputer


def get_forecast(geographical_label: str) -> Optional[ForecastView]:
    location: Optional[Location] = LocationProvider.get_location(geographical_label)

    if location is None:
        return None

    forecast: Forecast = ForecastProvider.get_forecast(location)
    pollution: Optional[Pollution] = PollutionProvider.get_pollution(location)

    res: List[WeatherView] = []

    for weather in forecast.forecast:
        wind_designation: str = WindDesignationComputer.compute_wind_designation(weather.wind)
        pollution_view = None
        if pollution is not None and weather.value_date == pollution.value_date:
            pollution_view = PollutionViewFactory.pollution_to_pollution_view(pollution)
        res.append(WeatherView(
            value_date=weather.value_date,
            main=weather.main,
            description=weather.description,
            temperature=weather.temperature,
            wind=WindView(weather.wind, wind_designation),
            cloudiness=weather.cloudiness,
            humidity=weather.humidity,
            pollution=pollution_view
        ))

    return ForecastView(forecast=res, location=location)

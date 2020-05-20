from weather_info.domain.forecast.Forecast import Forecast
from weather_info.domain.location.Location import Location
from weather_info.infrastructure.open_weather_map import OpenWeatherMapService


def get_forecast(location: Location) -> Forecast:
    return OpenWeatherMapService.get_forecast_from_location(location)

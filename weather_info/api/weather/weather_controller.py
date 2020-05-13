from typing import Optional

from flask_accepts import responds
from flask_restx import Namespace, Resource, abort

from weather_info.api.weather.model.WeatherSchema import WeatherSchema
from weather_info.application.weather import WeatherService
from weather_info.domain.weather.Weather import Weather

api = Namespace("Weather", description="Get weather for location")


@api.route("/<string:locationLabel>")
@api.param("locationLabel")
class WeatherResource(Resource):
    """ Weather """

    @responds(schema=WeatherSchema)
    def get(self, locationLabel: str) -> Optional[Weather]:
        res = WeatherService.get_weather(locationLabel)

        if res is None:
            return abort(404, message="Location not found on our provider (OpenCageData)")

        return res

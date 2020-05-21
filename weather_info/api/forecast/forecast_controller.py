from typing import Optional

from flask_accepts import responds
from flask_restx import Namespace, Resource, abort

from weather_info.api.forecast.model.ForecastSchema import ForecastSchema
from weather_info.application.forecast import ForecastService
from weather_info.application.forecast.ForecastView import ForecastView

api = Namespace("Forecast", description="Get forecast for location")


@api.route("/<string:locationLabel>")
@api.param("locationLabel")
class ForecastResource(Resource):
    """ Weather """

    @responds(schema=ForecastSchema)
    def get(self, locationLabel: str) -> Optional[ForecastView]:
        res = ForecastService.get_forecast(locationLabel)

        if res is None:
            return abort(404, message="Location not found on our provider (OpenCageData)")

        return res

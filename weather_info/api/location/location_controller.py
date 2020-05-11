from typing import Optional

from flask_accepts import responds
from flask_restx import Namespace, Resource, abort

from weather_info.api.location.model.LocationModel import LocationSchema
from weather_info.domain.location import LocationProvider
from weather_info.domain.location.Location import Location

api = Namespace("Location", description="Get locations")


@api.route("/<string:locationLabel>")
@api.param("locationLabel")
class LocationResource(Resource):
    """ Location """

    @responds(schema=LocationSchema)
    def get(self, locationLabel: str) -> Optional[Location]:
        """ Get a location """

        res = LocationProvider.get_location(locationLabel)

        if res is None:
            return abort(404, message="Location not found on our provider (OpenCageData)")

        return res

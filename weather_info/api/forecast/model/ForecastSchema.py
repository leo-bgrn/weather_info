from marshmallow import Schema, fields

from weather_info.api.forecast.model.WeatherSchema import WeatherSchema
from weather_info.api.location.model.LocationSchema import LocationSchema


class ForecastSchema(Schema):
    """ Forecast Schema """

    forecast = fields.Nested(WeatherSchema, many=True, attribute="forecast")
    location = fields.Nested(LocationSchema, attribute="location")

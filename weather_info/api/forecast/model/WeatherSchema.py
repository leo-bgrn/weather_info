from marshmallow import Schema, fields

from weather_info.api.location.model.LocationSchema import LocationSchema
from weather_info.api.forecast.model.TemperatureSchema import TemperatureSchema
from weather_info.api.forecast.model.WindSchema import WindSchema


class WeatherSchema(Schema):
    """ Weahter Schema """

    valueDate = fields.Date(attribute="value_date")
    main = fields.String(attribute="main")
    description = fields.String(attribute="description")
    temperature = fields.Nested(TemperatureSchema, attribute="temperature")
    wind = fields.Nested(WindSchema, attribute="wind")
    cloudiness = fields.Float(attribute="cloudiness")
    humidity = fields.Float(attribute="humidity")

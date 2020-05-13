from marshmallow import Schema, fields

from weather_info.api.location.model.LocationSchema import LocationSchema
from weather_info.api.weather.model.TemperatureSchema import TemperatureSchema
from weather_info.api.weather.model.WindSchema import WindSchema


class WeatherSchema(Schema):
    """ Weahter Schema """

    location = fields.Nested(LocationSchema, attribute="location")
    main = fields.String(attribute="main")
    description = fields.String(attribute="description")
    temperature = fields.Nested(TemperatureSchema, attribute="temperature")
    wind = fields.Nested(WindSchema, attribute="wind")
    cloudiness = fields.Float(attribute="cloudiness")
    humidity = fields.Float(attribute="humidity")

from marshmallow import Schema, fields


class TemperatureDataSchema(Schema):
    """ Temperature Data Schema """

    temp = fields.Integer(attribute="temp")
    feelsLike = fields.Integer(attribute="feels_like")


class TemperatureSchema(Schema):
    """ Temperature Schema """

    min = fields.Integer(attribute="min")
    max = fields.Integer(attribute="max")
    morning = fields.Nested(TemperatureDataSchema, attribute="morning")
    day = fields.Nested(TemperatureDataSchema, attribute="day")
    evening = fields.Nested(TemperatureDataSchema, attribute="evening")
    night = fields.Nested(TemperatureDataSchema, attribute="night")
    unit = fields.String(attribute="unit")

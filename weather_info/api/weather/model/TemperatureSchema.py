from marshmallow import Schema, fields


class TemperatureSchema(Schema):
    """ Temperature Schema """

    temperature = fields.Integer(attribute="main")
    feelsLike = fields.Integer(attribute="feels_like")
    min = fields.Integer(attribute="min")
    max = fields.Integer(attribute="max")
    unit = fields.String(attribute="unit")

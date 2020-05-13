from marshmallow import Schema, fields

from weather_info.api.location.model.CoordinatesSchema import CoordinatesSchema


class LocationSchema(Schema):
    """ Location model """

    label = fields.String(attribute="label")
    country = fields.String(attribute="country")
    coordinates = fields.Nested(CoordinatesSchema, attribute="coordinates")
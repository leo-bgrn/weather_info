from marshmallow import Schema, fields


class CoordinatesSchema(Schema):
    """ Coordinates Schema """

    latitude = fields.Float(attribute="latitude")
    longitude = fields.Float(attribute="longitude")
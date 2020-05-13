from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from weather_info.domain.location.CardinalPoint import CardinalPoint


class WindSchema(Schema):
    """ Wind Schema """

    speed = fields.Float(attribute="speed")
    direction = EnumField(CardinalPoint, attribute="cardinal_point")
    unit = fields.String(attribute="unit")

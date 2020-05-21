from marshmallow import Schema, fields


class PollutionSchema(Schema):
    """ Pollution Schema """

    airQualityLevelAqius = fields.Integer(attribute="air_quality_level_aqius")
    airQualityLevelOfConcern = fields.String(attribute="air_quality_level_of_concern")
    airQualityDescription = fields.String(attribute="air_quality_description")

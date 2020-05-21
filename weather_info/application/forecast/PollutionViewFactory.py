from weather_info.application.forecast.PollutionView import PollutionView
from weather_info.domain.pollution.Pollution import Pollution

pollutions_description = [
    {
        "level_of_concern": "Good",
        "min_value": 0,
        "max_value": 50,
        "description": "Air quality is satisfactory, and air pollution poses little or no risk."
    },
    {
        "level_of_concern": "Moderate",
        "min_value": 51,
        "max_value": 100,
        "description": "Air quality is acceptable. However, there may be a risk for some people, particularly those who are unusually sensitive to air pollution."
    },
    {
        "level_of_concern": "Unhealthy for Sensitive Groups",
        "min_value": 101,
        "max_value": 150,
        "description": "Members of sensitive groups may experience health effects. The general public is less likely to be affected."
    },
    {
        "level_of_concern": "Unhealthy",
        "min_value": 151,
        "max_value": 200,
        "description": "Some members of the general public may experience health effects; members of sensitive groups may experience more serious health effects."
    },
    {
        "level_of_concern": "Very Unhealthy",
        "min_value": 201,
        "max_value": 300,
        "description": "Health alert: The risk of health effects is increased for everyone."
    },
    {
        "level_of_concern": "Hazardous",
        "min_value": 301,
        "max_value": 100000000,
        "description": "Health warning of emergency conditions: everyone is more likely to be affected."
    }
]


def pollution_to_pollution_view(pollution: Pollution) -> PollutionView:
    for pollution_description in pollutions_description:
        if pollution.air_quality_level_aqius <= pollution_description["max_value"]:
            if pollution.air_quality_level_aqius >= pollution_description["min_value"]:
                return PollutionView(
                    air_quality_level_aqius=pollution.air_quality_level_aqius,
                    air_quality_level_of_concern=pollution_description["level_of_concern"],
                    air_quality_description=pollution_description["description"]
                )

    return PollutionView(
        air_quality_level_aqius=pollution.air_quality_level_aqius,
        air_quality_level_of_concern="Unknown",
        air_quality_description=""
    )

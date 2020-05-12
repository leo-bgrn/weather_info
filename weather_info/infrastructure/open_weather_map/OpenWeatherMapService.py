from weather_info.domain.location.CardinalPoint import CardinalPoint
from weather_info.domain.location.Location import Location
from weather_info.domain.weather.Temperature import Temperature
from weather_info.domain.weather.Weather import Weather
from weather_info.domain.weather.Wind import Wind
from weather_info.infrastructure.open_weather_map.OpenWeatherMapClient import client


def get_weather_from_location(location: Location) -> Weather:
    response = client.get_weather_for_coordinates(latitude=location.coordinates.latitude,
                                                  longitude=location.coordinates.longitude)

    return Weather(
        location=location,
        main=response["weather"][0]["main"],
        description=response["weather"][0]["description"],
        temperature=Temperature(
            main=response["main"]["temp"],
            feels_like=response["main"]["feels_like"],
            min=response["main"]["temp_min"],
            max=response["main"]["temp_max"]
        ),
        wind=Wind(
            speed=response["wind"]["speed"],
            cardinal_point=CardinalPoint.of(response["wind"]["deg"])
        ),
        cloudiness=response["clouds"]["all"],
        humidity=response["main"]["humidity"]
    )

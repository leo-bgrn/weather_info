from weather_info.domain.wind.Wind import Wind


def compute_wind_designation(wind: Wind) -> str:
    if wind.unit == "meter/sec":
        if wind.speed < 0.5:
            return "Calm"
        if wind.speed < 1.5:
            return "Light Air"
        if wind.speed < 3:
            return "Light Breeze"
        if wind.speed < 5.5:
            return "Gentle Breeze"
        if wind.speed < 8:
            return "Moderate Breeze"
        if wind.speed < 10.5:
            return "Fresh Breeze"
        if wind.speed < 14:
            return "Strong Breeze"
        if wind.speed < 17:
            return "Moderate Gale"
        if wind.speed < 20.5:
            return "Fresh Gale"
        if wind.speed < 24:
            return "Strong Gale"
        if wind.speed < 28:
            return "Whole Gale"
        if wind.speed < 32.5:
            return "Storm"
        return "Hurricane"
    else:
        raise ValueError(f"Unable to compute wind designation with the following unit : {wind.unit}")
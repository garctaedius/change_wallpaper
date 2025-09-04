import requests
from datetime import timezone, timedelta, datetime

# Categories are: Clear, Light Clouds, Overcast, Light Rain, Downpour, Thunderstorm, Snow
def map_weather_to_category(main, description):
    main = main.lower()
    description = description.lower()

    if main == "clear":
        return "Clear"
    elif main == "clouds":
        if "few" in description or "scattered" in description:
            return "Light Clouds"
        else:
            return "Overcast"
    elif main in ["rain", "drizzle"]:
        if "heavy" in description or "shower" in description:
            return "Downpour"
        else:
            return "Light Rain"
    elif main == "thunderstorm":
        return "Thunderstorm"
    elif main == "snow":
        return "Snow"
    else:
        return "Overcast"  # Default fallback

def get_sun_times(data):
    timezone_offset, sunrise, sunset = data["timezone"], data["sys"]["sunrise"], data["sys"]["sunset"]
    local_tz = timezone(timedelta(seconds=timezone_offset))
    now_local = datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(local_tz)
    sunrise_local = datetime.fromtimestamp(sunrise, tz=timezone.utc).astimezone(local_tz)
    sunset_local = datetime.fromtimestamp(sunset, tz=timezone.utc).astimezone(local_tz)
    return now_local, sunrise_local, sunset_local

# Categories are: Dawn/Dusk, Day, Night 
def map_sunrise_sunset_to_category(current, sunrise, sunset):
    dawn_start = sunrise - timedelta(minutes=60)
    dawn_end = sunrise + timedelta(minutes=60)
    dusk_start = sunset - timedelta(minutes=60)
    dusk_end = sunset + timedelta(minutes=60)

    if dawn_start <= current <= dawn_end or dusk_start <= current <= dusk_end:
        return "Dawn/Dusk"
    elif dawn_end < current < dusk_start:
        return "Day"
    else:
        return "Night"

def get_category():
    """Uses openweathermap to get the current weather and sunrise/sunset time at the set location."""
    import os
    from dotenv import load_dotenv
    load_dotenv()

    API_key = os.getenv("API_KEY")
    lat, lon = os.getenv("LAT"), os.getenv("LON")

    URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}&units=metric"
    response = requests.get(URL)

    if response.status_code == 200:  # Success
        data = response.json()

        weather_main = data["weather"][0]["main"]
        weather_description = data["weather"][0]["description"]
        weather_category = map_weather_to_category(weather_main, weather_description)

        now_local, sunrise_local, sunset_local = get_sun_times(data)
        time_category = map_sunrise_sunset_to_category(now_local, sunrise_local, sunset_local)
        
        return weather_category, time_category
    else:
        raise ConnectionError(f"Error collecting data from openweathermap. {response.status_code}")
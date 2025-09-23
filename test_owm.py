import os
from dotenv import load_dotenv

from get_category import get_category

def test():
    weather_category, time_category = get_category()
    load_dotenv()
    lat, lon = os.getenv("LAT"), os.getenv("LON")
    print(f"Successfully read weather at coordinates: {lat}, {lon}")
    print(f"Current weather: {weather_category}.")
    print(f"Current time of day: {time_category}.")

if __name__ == "__main__":
    test()
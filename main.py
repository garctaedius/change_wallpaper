from get_category import get_category
from change_wallpaper import change_wallpaper

def main():
    weather_category, time_category = get_category()

    wallpaper_dict = {
        "Dawn/Dusk": {
            "Clear": [], 
            "Light Clouds": [],
            "Overcast": [],
            "Light Rain": [],
            "Downpour": [],
            "Thunderstorm": [],
            "Snow": []
        },
        "Day": {
            "Clear": [], 
            "Light Clouds": [],
            "Overcast": [],
            "Light Rain": [],
            "Downpour": [],
            "Thunderstorm": [],
            "Snow": []
        },
        "Night": {
            "Clear": [], 
            "Light Clouds": [],
            "Overcast": [],
            "Light Rain": [],
            "Downpour": [],
            "Thunderstorm": [],
            "Snow": []
        }
    }

    potential_wallpapers = wallpaper_dict[time_category][weather_category]

    import random
    wallpaper = random.choice(potential_wallpapers)

    if not should_set_new_wallpaper(wallpaper, weather_category, time_category):
        return

    change_wallpaper(wallpaper)

def should_set_new_wallpaper(new_wallpaper, new_weather_category, new_time_category):
    """Returns False if the weather category has not changed or if the wallpaper has not changed. Otherwise returns True."""
    import pickle, os
    cache_file = "cache.pkl"

    data = None

    if os.path.exists(cache_file):
        try:
            with open(cache_file, 'rb') as f:
                data = pickle.load(f)
        except (pickle.UnpicklingError, EOFError, Exception) as e:
            pass
    else:
        pass
    
    if data is not None and len(data) == 3:
        current_wallpaper, current_weather_category, current_time_category = data

        if current_weather_category == new_weather_category and current_time_category == new_time_category:
            return False
        if current_wallpaper == new_wallpaper:
            return False

    with open(cache_file, "wb") as f:
        pickle.dump([new_wallpaper, new_weather_category, new_time_category], f)

    return True

if __name__ == "__main__":
    main()
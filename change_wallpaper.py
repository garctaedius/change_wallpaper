import subprocess

def change_wallpaper(new_w):
    import os
    from dotenv import load_dotenv
    load_dotenv()

    exe_path = os.getenv("WALLPAPER_ENGINE_EXE")
    wallpapers_path = os.getenv("WALLPAPERS_PATH")
    width = os.getenv("WIDTH")
    height = os.getenv("HEIGHT")
    wallpaper_file = wallpapers_path + fr"\{new_w}\project.json"

    command = [
        exe_path,
        "-control", "openWallpaper",
        "-file", wallpaper_file,
        "-width", width,
        "-height", height
    ]

    subprocess.run(command)
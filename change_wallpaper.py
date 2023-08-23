import os
import time

def change_wallpaper(image_path):
    # Change wallpaper using osascript command
    os.system(f"osascript -e 'tell application \"System Events\" to set picture of every desktop to \"{image_path}\"'")

# update your wallpaper folder path on the line below:
wallpaper_folder = "path/to/your/wallpaper/folder" 
wallpapers = os.listdir(wallpaper_folder)

while True:
    for wallpaper in wallpapers:
        wallpaper_path = os.path.join(wallpaper_folder, wallpaper)
        change_wallpaper(wallpaper_path)
        time.sleep(3600)  # Change wallpaper every hour

import time
import os    


# folder path
dir_path = '/home/bardia/Documents/python/background-changer/wallpapers'

found_pictures = []


# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        directory_path = dir_path + "/" + path    
        found_pictures.append(directory_path)



while True:
    for p in found_pictures:
        os.system(f"gsettings set org.gnome.desktop.background picture-uri file://{p}")
        print('Done')
        time.sleep(60)
        

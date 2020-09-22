import os
from PIL import Image

dir = './Test_images/'
for file in os.listdir(dir):
    if file.endswith('.jpg'):
        img = Image.open(f"{dir}{file}")
        name = file[:-4]
        img.rotate(270).resize((300,300)).save(f"{dir}{name}.png") 
        
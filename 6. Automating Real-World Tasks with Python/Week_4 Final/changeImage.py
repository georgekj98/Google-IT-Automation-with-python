#!/usr/bin/env python3

import os
from PIL import Image

dir = './supplier-data/images/'
for file in os.listdir(dir):
  try:
    if file.endswith('.tiff'):
        img = Image.open("{}{}".format(dir,file))
        name = file[:-5]
        img.resize((600,400)).convert("RGB").save("{}{}.jpeg".format(dir,name))
  except Exception as e:
        print(e)

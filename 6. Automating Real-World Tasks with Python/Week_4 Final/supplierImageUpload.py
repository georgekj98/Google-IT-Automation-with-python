#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
dir =  "./supplier-data/images/"

for  file in os.listdir(dir):
  try:
    if file.endswith('.jpeg'):
      with open("{}{}".format(dir,file), 'rb') as opened:
        r = requests.post(url, files={'file': opened})
  except Exception as e:
    print(e)






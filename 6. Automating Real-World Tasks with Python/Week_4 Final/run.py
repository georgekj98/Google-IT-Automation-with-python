#! /usr/bin/env python3
import os
import requests

dir = "./supplier-data/descriptions/"
url = "http://34.67.56.215/fruits/"

for file in os.listdir(dir):
    try:
        if file.endswith('.txt'):
            with open("{}{}".format(dir,file),'r') as f:
                text = f.read().split('\n')
                fruit = dict()
                fruit["name"] = text[0]
                fruit["weight"] = int(text[1].strip("lbs"))
                fruit["description"] = text[2]
                fruit["image_name"] = file.strip("txt")+"jpeg"
                response = requests.post(url, json = fruit)
                print(response.status_code)
    except Exception as e:
        print(e)













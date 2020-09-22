#! /usr/bin/env python3
import os
import requests
import json

#feedback list and writing to json file not needed for assesment
feedbacks = []
path = "./data/feedback/"
url = "http://<corpweb-external-IP>/feedback"

for f in os.listdir(path):
    f = path +f
    file = open(f,mode='r')
    text = file.read().split('\n')
    feed = dict()
    feed["title"] = text[0]
    feed["name"] = text[1]
    feed["date"] = text[2]
    feed["feedback"] = text[3]
    response = requests.post(url,json = feed)
    print(response.status_code)
    feedbacks.append(feed)
    file.close()

# not needed for assesment
with open('feedback.json', mode='w') as fb:
    json.dump(feedbacks,fb,indent=2)

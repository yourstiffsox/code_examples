import requests
import os
url = 'http://localhost/upload/'
for image in os.listdir('/studentid/supplier-data/images'):
    with open(image):
        if '.jpeg' in image:
            r = requests.post(url, files={'file': image})

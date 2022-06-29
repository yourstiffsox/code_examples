import os 
import requests

json = []
path = '/test_folder/'
for file in os.listdir('/test_folder'):
    with open(path + file) as f:
        temp_dict = {}
        text = f.readlines()
        temp_dict['name'] = text[0].strip()
        temp_dict['weight'] = int(text[1].strip())
        temp_dict['description'] = text[2].strip()
        temp_dict['image_name'] = file.split('.')[0] + '.jpeg'
        json.append(temp_dict)
for dictionary in json:
    url = 'http://localhost/upload/'
    r = requests.post(url, data=dictionary)
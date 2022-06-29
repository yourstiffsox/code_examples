import os
from PIL import Image

path = '/test_pictures/'

for file in os.listdir(path):
    
    im = Image.open(path + file)
    im = im.convert('RGB')
    new_size = 600,400
    im = im.resize(new_size)
    im.save(path + file.split('.')[0] + '.jpeg')

#!/usr/bin/env python3
import imp
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module
#35.226.214.171
def get_image_paths(mypath):
    return [ os.path.abspath(os.path.join(mypath, f)) 
    for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f)) and f.endswith("jpeg")]


url = "http://35.226.214.171/upload/"


#with open('/usr/share/apache2/icons/icon.sheet.png', 'rb') as opened:
    #r = requests.post(url, files={'file': opened})

def upload_image(image_list):
    for image in image_list:
        with open(image, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
        print(r.text)
        
upload_image(get_image_paths("./supplier-data/images"))
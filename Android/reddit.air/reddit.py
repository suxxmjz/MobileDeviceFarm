# -*- encoding=utf8 -*-

__author__ = "munib"

from airtest.core.api import *
import os
import sys
from PIL import Image
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")

#### Assumptions
## App is opened on home page and user is logged in


# You can specify to connect to a specific device, or create an adb bridge with a random device. using dev = device() method call.
#dev = connect_device("Android:///")

times_to_scroll = 100

print('Python Version')
print(sys.version)

apkFolderName = 'apk/' ## Doesn't change unless you move the apk elsewhere
apkFileName = 'reddit.apk'
packageName = 'com.reddit.frontpage'

def startApp():
    start_app(packageName)

def login():
    result1 =  exists(Template(r"signPrompt.jpg", resolution=(1080, 2400)))

    if type(result1) is bool:
        print('No sign in prompt')
    else:
        touch(result1)
    
    result2 =  exists(Template(r"skip.jpg", resolution=(1080, 2400)))
    if type(result2) is bool:
        print('No skip')
    else:
        touch(result2)
        print("in app")
        
def uploadAd(fp, ip_address, latitude, longitude, epoch_time, source):
    url = os.getenv("URL")
    
    files = {'ad': open(fp, 'rb')}
    print(files)
    
    multipart_form_data = {
        'ad': ('ad.png', open(fp, 'rb')),
        'ip_address': (None, ip_address),
        'platform': (None, 'MOBILE'),
        'type': (None, 'STATIC'),
        'latitude': (None, latitude),
        'longitude': (None, longitude),
        'source': (None, source),
        'time_stamp':  (None, str(epoch_time))
    }
    response = requests.post(url, files=multipart_form_data)
    print(response.json())
    print(response.text)

def scrapAds():

    while(1):
        
        ## Implement ad specific triggers here.
        result =  exists(Template(r"tpl123456789.png", record_pos=(-0.263, -0.605), resolution=(1080, 2400)))

        if type(result) is bool:
            print('Not an ad.')
        else:
            # adjust ad
            (x, y) = result
            print(result)
            # checks to see if ad is too low
            if y > 300:
                swipe([x,y], [x, 300])
            time.sleep(1)
            epoch_time = int(time.time())
            try:
                os.mkdir('RedditAds')
            except:
                print("Directory already exists")
            finally:
                epochTime = str(epoch_time)
                filePath = 'RedditAds/' + epochTime + '.png'
                device().snapshot(filename= filePath)
                
                print("Saved ad, path")
                print(filePath)
                
                im = Image.open(filePath)
                
                print(im)
                
                width, height = im.size 
                
                print("height")
                print(height)
                print("width")
                print(width)
                
                left = 0
                top = 230
                right = 675
                bottom = 906
                
                im1 = im.crop((left, top, right, bottom))
                
                im1.save(filePath)
                
                uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("REDDIT_SOURCE"))

        swipe([880,2000], [880, 250])
    
    
login()
scrapAds()




# -*- encoding=utf8 -*-

__author__ = "Sukriti"

from airtest.core.api import *
import os
import sys
from PIL import Image
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values
load_dotenv()
config = dotenv_values(".env")



print('Python Version')
print(sys.version)

packageName = 'com.pinterest'


def login():
    
    result1 =  exists(Template(r"email.jpg", resolution=(1080, 2400)))
    if type(result1) is bool:
        print('no input for email')
    else:
        touch(result1)
        time.sleep(1)
        text(os.getenv("PINTEREST_USER"))
        time.sleep(3)

    result2 =  exists(Template(r"continue.jpg", resolution=(1080, 2400)))
    if type(result2) is bool:
        print('no continue button')
    else:
        touch(result2)
        time.sleep(1)
    
    result3 =  exists(Template(r"password.jpg", resolution=(1080, 2400)))
    if type(result3) is bool:
        print('no input for password')
    else:
        touch(result3)
        time.sleep(1)
        text(os.getenv("PINTEREST_PASSWORD"))
        time.sleep(3)
    
    result4 =  exists(Template(r"login.jpg", resolution=(1080, 2400)))
    if type(result4) is bool:
        print('no login button')
    else:
        touch(result4)
        time.sleep(1)


def checkState():
    stateFeed = exists(Template(r"checkState.jpg", resolution=(1080, 1920))) or exists(Template(r"browse.jpg", resolution=(1080, 1920)))

    if type(stateFeed) is bool:
        stop_app(packageName)
        time.sleep(1)
        start_app(packageName)
        time.sleep(1)
        resultLogin =  exists(Template(r"email.jpg", resolution=(1080, 2400)))
        if type(resultLogin) is bool:
            pass
        else:
            login()

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

def checkForAd():

    ## Implement ad specific triggers here.
    checkState()
    result =  exists(Template(r"promoted.jpg",resolution=(1080, 2400)))

    if type(result) is bool:
        print('Not an ad.')
    else:
        try:
            os.mkdir('PinterestAds')
        except:
            print("Directory already exists")
        finally:
            touch(result)
            time.sleep(8)
            epoch_time = int(time.time())
            epochTime = str(epoch_time)
            filePath = 'PinterestAds/' + epochTime + '.jpg'
            device().snapshot(filename= filePath)
            print("Saved ad")

            uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("PINTEREST_SOURCE"))

            touch([99, 199])
            


## This function will visit a random pin then exit back to the home feed.
def visitRandomPin():
    touch([584, 1361])
    time.sleep(5)
    touch([99, 199])
        
        
def scrollFeed():
    x = 55
    y = 2117
    for x in range(0, 100):
        sleep(1)
        checkForAd()
        swipeUp = swipe([x,y], [x, 300])
        visitRandomPin()

login()
scrollFeed()
# -*- encoding=utf8 -*-
__author__ = "munib"


from airtest.core.api import *
import os
import sys
import random
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values
from PIL import Image

load_dotenv()
config = dotenv_values(".env")


#init_device("Android")

print('Python Version')
print(sys.version)

# This device has a genuine facebook account.
#dev = connect_device("Android:///")

apkFolderName = 'apk/'
apkFileName = 'facebook.apk'
packageName = 'com.facebook.katana'

def login():
    fbemail=  exists(Template(r"fbemail.jpg", resolution=(1080, 2400)))
    if type(fbemail) is bool:
        print('No email prompt')
    else:
        touch(fbemail)
        time.sleep(1)
        text(os.getenv("FBUSER"))
        time.sleep(3)

    fbpass=  exists(Template(r"fbpassword.jpg", resolution=(1080, 2400)))
    if type(fbpass) is bool:
        print('No password prompt')
    else:
        touch(fbpass)
        time.sleep(1)
        text(os.getenv("FBPASSWORD"))
        time.sleep(3)

    fblogin =  exists(Template(r"fblogin.jpg", resolution=(1080, 2400)))
    if type(fblogin) is bool:
        print('No sign in prompt')
    else:
        touch(fblogin)
        time.sleep(10)

    fbskip =  exists(Template(r"fbskip.jpg", resolution=(1080, 2400)))
    if type(fbskip) is bool:
        print('No skip')
    else:
        touch(fbskip)
        time.sleep(3)

    fbskip2 =  exists(Template(r"fbskip2.jpg", resolution=(1080, 2400)))
    if type(fbskip2) is bool:
        print('No skip')
    else:
        touch(fbskip2)
        time.sleep(3)
    
    fbskip3 =  exists(Template(r"fbskip2.jpg", resolution=(1080, 2400)))
    if type(fbskip3) is bool:
        print('No skip')
    else:
        touch(fbskip3)
        time.sleep(3)

    notNow =  exists(Template(r"notNow.jpg", resolution=(1080, 2400)))
    if type(notNow) is bool:
        print('No notNow')
    else:
        touch(notNow)
        time.sleep(2)
    
    notNow2 =  exists(Template(r"notNow2.jpg", resolution=(1080, 2400)))
    if type(notNow2) is bool:
        print('No notNow')
    else:
        touch(notNow2)
        time.sleep(2)

    denyLoc =  exists(Template(r"denyLocation.jpg", resolution=(1080, 2400)))
    if type(denyLoc) is bool:
        print('No deny location')
    else:
        touch(denyLoc)
    
    notNowLoc =  exists(Template(r"notNowLoc.jpg", resolution=(1080, 2400)))
    if type(notNowLoc) is bool:
        print('No notNowLoc')
    else:
        touch(notNowLoc)
        time.sleep(2)

    fbdeny =  exists(Template(r"fbdeny.jpg", resolution=(1080, 2400)))
    if type(fbdeny) is bool:
        print('No deny')
    else:
        touch(fbdeny)
        time.sleep(1)

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

def interactWithPost():
    # If something isn't an add, we want to randomly interact with it.
    # This makes the scrapper more human-like by randomly liking posts
    if random.randint(0, 100) < 50:
        print("Like the picture")
        heartIcon =  exists(Template(r"tpl1620419948304.png", record_pos=(-0.373, 0.254), resolution=(1080, 2400)))

        if (type(heartIcon)) is bool:
            print("Can't like anything, move on")
        else:
            (x, y) = heartIcon
            # We dont care about the favourite logo, just care about the like on posts
            touch(heartIcon)

def adjustAd():
    result = exists(Template(r"tpl1588193935119.jpg", record_pos=(-0.258, -0.156), resolution=(1080, 1920)))

    
    if type(result) is bool:
        print(result)
        print('Not an ad.')
        interactWithPost()
    else:
        (x, y) = result
        print(x)
        print(y)
        swipeUp = swipe([x,y], [x, 300])

def checkState():
    # Check to see if indeed were on the scrapping page, if that is not the case, then we need
    # to reset the app to the original state by restarting it.
    state = exists(Template(r"tpl1620419728990.png", record_pos=(-0.413, -0.833), resolution=(1080, 2400)))


    if type(state) is bool:
        print("State has been lost, reset it.")
        fbemailState=  exists(Template(r"fbemail.jpg", resolution=(1080, 2400)))
        if type(fbemailState) is bool:
            print('No email prompt')
            time.sleep(1)
            stop_app(packageName)
            time.sleep(1)
            start_app(packageName)
            time.sleep(1)
        else:
            login()

def scrapAds():

    while(1):
        checkState()
        result =  exists(Template(r"tpl1588193935119.jpg", record_pos=(-0.258, -0.156), resolution=(1080, 1920)))

        if type(result) is bool:
            print(result)
            print('Not an ad.')
        else:
            (x, y) = result
            print(x)
            print(y)
            swipeUp = swipe([x,y], [x, 300])
            adjustAd()
            print('***swiped up')
            print(swipeUp)
            time.sleep(1)
            epoch_time = int(time.time())

            try:
                os.mkdir('FacebookAds')
            except:
                print("Directory already exists")
            finally:
                epochTime = str(epoch_time)
                filePath = 'FacebookAds/' + epochTime + '.png'
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
                
                uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("FACEBOOK_SOURCE"))
            
        swipe([600,2000], [600, 0])

login()
scrapAds()


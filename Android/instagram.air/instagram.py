# -*- encoding=utf8 -*-

__author__ = "munib"

from airtest.core.api import *
import os
import sys
from PIL import Image
import requests
import random
from dotenv import load_dotenv
from dotenv import dotenv_values


load_dotenv()
config = dotenv_values(".env")
# This device has the only instagram account that isn't blocked

# dev = connect_device("Android:///")

print('Python Version')
print(sys.version)

apkFolderName = 'apk/'
apkFileName = 'instagram.apk'
packageName = 'com.instagram.android'


def followAccounts():
    touch(Template(r"tpl1594671516207.png", record_pos=(-0.202, 0.695), resolution=(1080, 1920)))

def loginApp():
    smallLogin = exists((Template(r"tpl1594669626855.png",resolution=(1080, 2400))))
    if type(smallLogin) is bool:
        print('Already logged in.')
    else:
        touch(smallLogin)
        time.sleep(2)
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

    IGemail = exists((Template(r"IGUser.png",resolution=(1080, 2400))))
    if type(IGemail) is bool:
        print("email login not found")
    else:
        touch(IGemail)
        time.sleep(1)
        text(os.getenv("FBUSER"))
        time.sleep(4)

    IGpass = exists((Template(r"IGPass.png",resolution=(1080, 2400))))
    if type(IGpass) is bool:
        print("password field not found")
    else:
        touch(IGpass)
        text(os.getenv("FBPASSWORD"))
        time.sleep(2)

    finalLogin = exists((Template(r"finalLogin.png",resolution=(1080, 2400))))
    if type(finalLogin) is bool:
        print("no login button")
    else:
        touch(finalLogin)
        time.sleep(5)
    
    continueButton = exists((Template(r"continue.jpg",resolution=(1080, 2400))))
    if type(continueButton) is bool:
        print("no continue button")
    else:
        touch(continueButton)
        time.sleep(10)
       
            
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

def adjustAd():
    result = exists(Template(r"tpl1594670972613.png", record_pos=(-0.277, -0.349), resolution=(1080, 1920)))

    
    if type(result) is bool:
        print(result)
        print('Not an ad.')
    else:
        (x, y) = result
        print(x)
        print(y)
        swipeUp = swipe([0,y], [0, 300])
        

def checkState():
    # Check to see if indeed were on the scrapping page, if that is not the case, then we need
    # to reset the app to the original state by restarting it.
    state = exists(Template(r"tpl1619629246177.png", record_pos=(-0.07, -0.748), resolution=(1080, 1920)))

    if type(state) is bool:
        print("State has been lost, reset it.")
        smallLoginState = exists((Template(r"tpl1594669626855.png",resolution=(1080, 2400))))
        if type(smallLoginState) is bool:
            stop_app(packageName)
            time.sleep(1)
            start_app(packageName)
            time.sleep(1)
        else:
            loginApp()

def interactWithPost():
    # If something isn't an add, we want to randomly interact with it.
    # This makes the scrapper more human-like by randomly liking posts
    if random.randint(0, 100) < 50:
        print("Like the picture")
        heartIcon =  exists(Template(r"tpl1619652861021.png", record_pos=(-0.423, 0.456), resolution=(1080, 1920)))
        if (type(heartIcon)) is bool:
            print("Can't like anything, move on")
        else:
            (x, y) = heartIcon
            # We dont care about the favourite logo, just care about the like on posts
            if (y < 500):
                touch(heartIcon)




def scrapAds():

#     swipeUp = swipe([0,y], [0, 300])
    while(1):
        checkState()

        # Check sponsored tag.
        result = exists(Template(r"tpl1594670972613.png", record_pos=(-0.277, -0.349), resolution=(1080, 1920)))

        if type(result) is bool:
            print(result)
            print('Not an ad.')
            interactWithPost()
        else:
            (x, y) = result
            print(x)
            print(y)
            swipeUp = swipe([0,y], [0, 300])
            adjustAd()
            print('***swiped up')
            print(swipeUp)
            time.sleep(1)
            epoch_time = int(time.time())
            try:
                os.mkdir('InstagramAds')
            except:
                print("Directory already exists")
            finally:
                epochTime = str(epoch_time)
                filePath = 'InstagramAds/' + epochTime + '.png'
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
                
                uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("INSTAGRAM_SOURCE"))
                
            
            
            

        swipe([880,1500], [880, 250])

#This function checks if we have reached the end of the feed. If so, it will go to the top and refresh it again.
# I was going to refresh the feed once instagram says you've reached the end but the problem is that we don't care about that at all.
# The feed is theoretically infinite so you won't even need to refresh it, for now I will leave this function in here regardless.
def refreshFeed():
    touch(Template(r"tpl1594679095671.png", record_pos=(-0.398, 0.697), resolution=(1080, 1920)))
    time.sleep(1)
    swipe([600,600], [600, 2000])



## Depending on which part I want to start, I can comment or uncomment that specific function
# followAccounts() #todo, do this at a later time when its necessary to be able to follow accounts aswell. Right now thats done manually
loginApp()
#login()
scrapAds()

# refreshFeed()

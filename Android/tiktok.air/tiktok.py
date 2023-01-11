

__author__ = "su"

from airtest.core.api import *
import os
import sys
import random
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")


print('Python Version')
print(sys.version)

# This new apk complies with privacy rules
packageName = 'com.ss.android.ugc.trill'

def startApp():
    start_app(packageName)


def login():
    #it doesn't actually login, it skips the login
    result1 =  exists(Template(r"agreeAndCont.jpg", resolution=(1080, 2400)))

    if type(result1) is bool:
        print('no terms and policy')
    else:
        touch(result1)
    
    result2 =  exists(Template(r"skip.jpg", resolution=(1080, 2400)))
    if type(result2) is bool:
        print('No skip')
    else:
        touch(result2)
    
    result3 =  exists(Template(r"startWatching.jpg", resolution=(1080, 2400)))

    if type(result3) is bool:
        print('No start watching')
    else:
        touch(result3)
    
    result4 =  exists(Template(r"exitLogin.jpg", resolution=(1080, 2400)))
    if type(result4) is bool:
        print('No exit login')
    else:
        touch(result4)
        print("in app")

## Function will swipe through videos
def navigateVideo():
    swipe((550, 1700), (550, 400))
    checkAd()
    

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

def likeVideo():
    print("liking video randomly")
    if random.randint(0, 50) % 2 == 0:
        touch((500, 1200), times=2)
        
def checkAd():
    checkState()
    print("checking to see if this is an ad")
    result = exists(Template(r"sponsored.jpg", resolution=(1080, 2400)))


    if type(result) is bool:
        print('Not an ad.')
    else:
        try:
            os.mkdir('TikTokAds')
        except:
            print("Directory already exists")
        finally:
            time.sleep(1)
            epoch_time = int(time.time())
            epochTime = str(epoch_time)
            filePath = 'TikTokAds/' + epochTime + '.png'
            device().snapshot(filename= filePath)
            
            print("Saved ad, path")
            print(filePath)
            
            uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("TIKTOK_SOURCE"))

def checkState():
    state = exists(Template(r"checkState1.jpg", resolution=(1080, 1920)))

    if type(state) is bool: 
        print("State has been lost, reset it.")
        stop_app(packageName)
        time.sleep(1)
        start_app(packageName)
        time.sleep(1)

       
## Main function that will run all the logic inside of it.
## Things such as liking the video - sleeping for a bit to be able to see the whole video
## and also things like checking if its an ad or not.
def captureAds():
    for x in range(0, 10000):
        time.sleep(5) # big sleep timer needed, or we get rate limited by tiktok.
        #likeVideo()
        navigateVideo()
    


    

## Depending on which part I want to start, I can comment or uncomment that specific function
#startApp()
login()
captureAds()







# -*- encoding=utf8 -*-

__author__ = "su"

from airtest.core.api import *
import os
import sys
from PIL import Image
import requests
from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()
config = dotenv_values(".env")


# You can specify to connect to a specific device, or create an adb bridge with a random device. using dev = device() method call.
#dev = connect_device("Android:///")

times_to_scroll = 10000

print('Python Version')
print(sys.version)


packageName = 'com.twitter.android'

def startApp():
    start_app(packageName)

def login():
    result1 =  exists(Template(r"smallLogin.jpg", resolution=(1080, 2400)))

    if type(result1) is bool:
        print('No login button')
    else:
        touch(result1)
    
    result2 =  exists(Template(r"email.jpg", resolution=(1080, 2400)))
    if type(result2) is bool:
        print('no input for email')
    else:
        touch(result2)
        time.sleep(1)
        text(os.getenv("TWITTER_USER"))
        time.sleep(3)

    result3 =  exists(Template(r"next.jpg", resolution=(1080, 2400)))
    if type(result3) is bool:
        print('no next button')
    else:
        touch(result3)
        time.sleep(1)
    
    result4 =  exists(Template(r"password.jpg", resolution=(1080, 2400)))
    if type(result4) is bool:
        print('no input for password')
    else:
        touch(result4)
        time.sleep(1)
        text(os.getenv("TWITTER_PASSWORD"))
        time.sleep(3)
    
    result5 =  exists(Template(r"finalLogin.jpg", resolution=(1080, 2400)))
    if type(result5) is bool:
        print('no input for email')
    else:
        touch(result5)
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
        checkState()
        ## Implement ad specific triggers here.
        result =  exists(Template(r"promoted.jpg", resolution=(1080, 2400)))
        if type(result) is bool:
            print('Not an ad.')
            swipe([880,1000], [880, 250])
        else:

            time.sleep(1)
            epoch_time = int(time.time())
            try:
                os.mkdir('TwitterAds')
            except:
                print("Directory already exists")
            finally:
                epochTime = str(epoch_time)
                filePath = 'TwitterAds/' + epochTime + '.png'
                device().snapshot(filename= filePath)
                
                print("Saved ad, path")
                print(filePath)
               
                
                uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("TWITTER_SOURCE"))

                swipe([880,2000], [880, 250])
                swipe([880,1000], [880, 250])
    
    
def checkState():
    state = exists(Template(r"checkState.jpg", resolution=(1080, 1920)))

    if type(state) is bool:
        print("State has been lost, reset it.")
        whiteHomeState = exists((Template(r"whiteHome.jpg",resolution=(1080, 2400))))
        if type(whiteHomeState) is bool:
            pass
        else:
            touch(whiteHomeState)
        loginState = exists((Template(r"smallLogin.jpg",resolution=(1080, 2400)))) or exists((Template(r"email.jpg",resolution=(1080, 2400)))) or exists((Template(r"password.jpg",resolution=(1080, 2400)))) or exists((Template(r"next.jpg",resolution=(1080, 2400))))
        if type(loginState) is bool:
            stop_app(packageName)
            time.sleep(1)
            start_app(packageName)
            time.sleep(1)
        else:
            login()

login()
scrapAds()




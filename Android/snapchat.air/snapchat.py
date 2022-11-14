

__author__ = "munib"

from airtest.core.api import *
import os
import sys
from dotenv import load_dotenv
from dotenv import dotenv_values
import requests

load_dotenv()
config = dotenv_values(".env")
print('Python Version')
print(sys.version)

packageName = 'com.snapchat.android'



def login():
    result1 = exists(Template(r"startLogin.jpg", resolution=(1080, 2400)))
    if type(result1) is bool:
        print('No login button')
    else:
        touch(result1)

    result2 = exists(Template(r"user.jpg", resolution=(1080, 2400)))
    if type(result2) is bool:
        print('No user button')
    else:
        touch(result2)
        time.sleep(1)
        text(os.getenv("SNAPCHAT_USER"))
        time.sleep(1)

    result3 = exists(Template(r"password.jpg", resolution=(1080, 2400)))
    if type(result3) is bool:
        print('No password button')
    else:
        touch(result3)
        time.sleep(1)
        text(os.getenv("SNAPCHAT_PASSWORD"))
        time.sleep(3)

    result4 = exists(Template(r"finalLogin.jpg", resolution=(1080, 2400)))
    if type(result4) is bool:
        print('No final login button')
    else:
        touch(result4)
    
    result5 = (Template(r"turnOn.jpg", resolution=(1080, 2400)))
    if type(result5) is bool:
        print('No turn on button')
    else:
        touch(result5)
        time.sleep(1)


    result6  = exists(Template(r"whileUsingApp.jpg", resolution=(1080, 2400)))
    if type(result6) is bool:
        print('No while using app button')
    else:
        touch(result6)
        time.sleep(2)

    result8 = exists(Template(r"allow.jpg", resolution=(1080, 2400)))
    if type(result8) is bool:
        print('No allow button')
    else:
        touch(result8)
        time.sleep(1)

    result9 = exists(Template(r"whileUsingApp.jpg", resolution=(1080, 2400)))
    if type(result9) is bool:
        print('No while using app button')
    else:
        touch(result9)
        time.sleep(2)
 

    result10 = exists(Template(r"stories.jpg", resolution=(1080, 2400)))
    if type(result10) is bool:
        print('No story page button')
    else:
        touch(result10)
        time.sleep(2)
    

    result11 = exists(Template(r"viewStory.jpg", resolution=(1080, 2400)))
    if type(result11) is bool:
        print('No stories')
    else:
        touch(result11)
        time.sleep(2)  

def checkState():
    state = exists(Template(r"arrow.jpg",resolution=(1080, 1920))) or exists(Template(r"camIcon.jpg",resolution=(1080, 1920))) or exists(Template(r"darkBell.jpg",resolution=(1080, 1920))) or exists(Template(r"whiteBell.jpg",resolution=(1080, 1920)))

    if type(state) is bool:
        print("State has been lost, reset it.")
        smallLoginState = exists((Template(r"user.jpg",resolution=(1080, 2400)))) or exists((Template(r"startLogin.jpg",resolution=(1080, 2400)))) or exists((Template(r"password.jpg",resolution=(1080, 2400))))
        if type(smallLoginState) is bool:
            stop_app(packageName)
            time.sleep(1)
            start_app(packageName)
            time.sleep(1)
            result12 = exists(Template(r"stories.jpg", resolution=(1080, 2400)))
            if type(result12) is bool:
                print('No story page button')
            else:
                touch(result12)
                time.sleep(2)
            

            result13 = exists(Template(r"viewStory.jpg", resolution=(1080, 2400)))
            if type(result13) is bool:
                print('No stories')
            else:
                touch(result13)
                time.sleep(2)

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
    while(1):
        checkState()
        result =  exists(Template(r"ad1.jpg",resolution=(1080, 2400))) or exists(Template(r"ad2.jpg",resolution=(1080, 2400)))

        if type(result) is bool:
            print('Not an ad.')
            touch((340, 770))
        else:
            try:
                os.mkdir('SnapchatAds')
            except:
                print("Directory already exists")
            finally:
                time.sleep(3)
                epoch_time = int(time.time())
                epochTime = str(epoch_time)
                filePath = 'SnapchatAds/' + epochTime + '.jpg'
                device().snapshot(filename= filePath)
                print("Saved ad")

                uploadAd(filePath, os.getenv("IP_ADDRESS"), os.getenv("LATITUDE"), os.getenv("LONGITUDE") ,epoch_time, os.getenv("SNAPCHAT_SOURCE"))

                touch((340, 770))

login()
checkForAd()

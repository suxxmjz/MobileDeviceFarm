# -*- encoding=utf8 -*-

__author__ = "munib"

from airtest.core.api import *
import os
import sys
import pathlib

#### TODOS
## Install instagram on device (done)
## login via credentials (not done)
## subscribe to new accounts (Maybe can use api for that? UI wise might be too hard - not done)
## Start scraping ads, once at bottom refresh feed and start agan.

# This device has the only facebook account that isn't blocked lol fingers crossed they don't block this one too
connect_device("Android:///" + "R58N33ETXKX")

print('Python Version')
print(sys.version)

# apkFolderName = 'apk/'
# apkFileName = 'youtube.apk'
packageName = 'com.google.android.youtube'

def followAccounts():
    touch(Template(r"tpl1594671516207.png", record_pos=(-0.202, 0.695), resolution=(1080, 1920)))
    
def startApp():
#     install(apkFolderName + apkFileName)
    start_app(packageName)


def login():
    continueButton = exists(Template(r"tpl1594669626855.png", record_pos=(-0.192, 0.014), resolution=(1080, 1920)))



    
    print(continueButton)
    if continueButton:
        print("Continue button exists, no need to login")
        dev.touch(continueButton)
        



def adjustAd():
    result = exists(Template(r"tpl1595360584308.png", record_pos=(-0.321, 0.246), resolution=(1080, 2400)))

    
    if type(result) is bool:
        print(result)
        print('Not an ad.')
    else:
        (x, y) = result
        print(x)
        print(y)
        swipeUp = swipe([x,y], [x, 1500])
        

def scrapAds():

    while(1):
        result =  exists(Template(r"tpl1595360584308.png", record_pos=(-0.321, 0.246), resolution=(1080, 2400)))



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
            dev = device()
            dev.snapshot(filename= 'ads/' + str(epoch_time) + '.png')
            print("Saved ad")

        swipe([880,2000], [880, 250])

        
        
        
        
    
#This function checks if we have reached the end of the feed. If so, it will go to the top and refresh it again.
# I was going to refresh the feed once instagram says you've reached the end but the problem is that we don't care about that at all.
# The feed is theoretically infinite so you won't even need to refresh it, for now I will leave this function in here regardless.
def refreshFeed():
    touch(Template(r"tpl1594679095671.png", record_pos=(-0.398, 0.697), resolution=(1080, 1920)))
    time.sleep(1)
    swipe([600,600], [600, 2000])

        
            

## Depending on which part I want to start, I can comment or uncomment that specific function
startApp()
# login()
# followAccounts() #todo, do this at a later time when its necessary to be able to follow accounts aswell.
scrapAds()
# refreshFeed()
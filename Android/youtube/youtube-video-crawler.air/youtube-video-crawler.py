# -*- encoding=utf8 -*-

__author__ = "munib"

from airtest.core.api import *
import os
import sys
import pathlib

#### TODOS
## Start app
## click on a random video that you see
## Check and see if ad is being shown
## if you see an ad, capture it.
## Otherwise scroll down and click on the next video

# This device has the only facebook account that isn't blocked
connect_device("Android:///" + "R58N33813BE")

print('Python Version')
print(sys.version)

# apkFolderName = 'apk/'
# apkFileName = 'youtube.apk'
packageName = 'com.google.android.youtube'

    
def startApp():
#     install(apkFolderName + apkFileName)
    start_app(packageName)
        
def stopApp():
    '''stops the app 
    '''
    stop_app(packageName)
        

def checkForAd():
    result =  exists(Template(r"tpl1595360584308.png", record_pos=(-0.321, 0.246), resolution=(1080, 2400)))



    if type(result) is bool:
        print('Not an ad.')
    else:
        time.sleep(1)
        epoch_time = int(time.time())
        dev = device()
        dev.snapshot(filename= 'ads/' + str(epoch_time) + '.png')
        print("Saved ad")


def skipForward():
    """ will skip the video forwad by 10 seconds
    achieved by double tapping the running vid on right side.
    """
    touch((965, 492), times=2)

    
def scrollSuggestedField():
    """ Will scroll through the suggested video feed, will only do it once, 
    so future support for multiple scroll can be added later
    """
    swipe([543, 2224], [543, 730])

def dismissVideo():
    swipe([954, 217], [954, 2050])
    touch((1000, 2050))
    
    
def clickVideo():
    '''Will click on a video.
    If the expected state isn't there, it will reset to the original state and try again.
    '''
    touch((480, 1862))

## Depending on which part I want to start, I can comment or uncomment that specific function
startApp()

for x in range(0, 100):
    scrollSuggestedField()
    clickVideo()
    checkForAd()
    dismissVideo()


# login()
# followAccounts() #todo, do this at a later time when its necessary to be able to follow accounts aswell.
# scrapAds()
# refreshFeed()
# skipForward()
# stopApp()
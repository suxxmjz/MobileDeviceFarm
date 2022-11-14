# -*- encoding=utf8 -*-
__author__ = "munib"

from airtest.core.api import *



from poco.drivers.unity3d import UnityPoco
poco = UnityPoco()
from airtest.core.android.base_touch import *
from airtest.core.android.rotation import XYTransformer

import os
import sys
import pathlib


connect_device("Android:///" + "R58N33ETXKX")

dev = device()

print('Python Version')
print(sys.version)


apkFolderName = 'apk/'
apkFileName = 'ASMR.apk'
packageName = 'com.crazylabs.asmr.cut'

install(apkFolderName + apkFileName)
start_app(packageName)
# sleep(5.0)

# assert_exists(Template(r"tpl1589245915183.png", record_pos=(0.421, 0.763), resolution=(1080, 1920)), "We see an ad")
 
#
# Full screen ads are shown like this. Video ads being shown.
# assertion = assert_exists(Template(r"tpl1589246268251.png", record_pos=(-0.476, 0.741), resolution=(1080, 1920)), "Please fill in the test point.")


#lh see if the X exists, if so, close the ad.
# cross = assert_exists(Template(r"tpl1589246687128.png", record_pos=(-0.418, -0.753), resolution=(1080, 1920)), "Please fill in the test point.")

# swipe([255,55], [255, 1600])

# os.makedirs(pathToFile, exist_ok=True)  

def swipeDown():
#     multitouch_event = [
#         DownEvent((588, 40), 0),
# #         SleepEvent(0.2),
#         MoveEvent((588, 1730)),
#         SleepEvent(0.2),
#         UpEvent(0)]
    
#     dev.minitouch.perform(multitouch_event)
#     sleep(1)
# The arguments are here
# https://github.com/AirtestProject/Airtest/blob/edf903941afee29d74a957318e26058eae330732/airtest/core/android/minitouch.py#L456
    swipe((588, 100), (588, 1730), duration=2, steps = 5)

def captureAd():
    sleep(1)
    epoch_time = int(time.time())
    dev.snapshot(filename= 'ads/' + str(epoch_time) + '.png')
    

def checkForAds():
    #Here we will check for all the possible types of ads. The same cross is being checked a few times over because it has slightly different variatons.
    #Once you capture the ad, come back, tap the x and start playing again.
    cross = exists(Template(r"tpl1590553519922.png", record_pos=(0.433, -0.841), resolution=(1080, 1920))) 
    
#     or exists(Template(r"tpl1590525024602.png", record_pos=(-0.327, 0.524), resolution=(1080, 1920))) or exists(Template(r"tpl1590524085392.png", record_pos=(0.447, -0.829), resolution=(1080, 1920))) or exists(Template(r"tpl1590522698864.png", record_pos=(0.402, -0.731), resolution=(1080, 1920))) or exists(Template(r"tpl1590520611083.png", record_pos=(0.437, -0.833), resolution=(1080, 1920)))  or exists(Template(r"tpl1590519524102.png", record_pos=(0.4, -0.731), resolution=(1080, 1920))) or exists(Template(r"tpl1590519372325.png", record_pos=(-0.421, -0.773), resolution=(1080, 1920))) or exists(Template(r"tpl1589586107842.png", record_pos=(-0.418, -0.757), resolution=(1080, 1920))) or exists(Template(r"tpl1589246687128.png", record_pos=(-0.418, -0.753), resolution=(1080, 1920))) or exists(Template(r"tpl1589587034924.png", record_pos=(-0.412, -0.797), resolution=(1080, 1920))) or exists(Template(r"tpl1590083156725.png", record_pos=(0.429, -0.815), resolution=(1080, 1920))) or exists(Template(r"tpl1590451993206.png", record_pos=(-0.207, 0.437), resolution=(1080, 1920))) or exists(Template(r"tpl1590518435555.png", record_pos=(-0.202, 0.416), resolution=(1080, 1920))) or exists(Template(r"tpl1589246268251.png", record_pos=(-0.476, 0.741), resolution=(1080, 1920)))  or exists(Template(r"tpl1591734361534.png", record_pos=(-0.146, 0.276), resolution=(1080, 2400)))



    
    if cross:
        captureAd()
        touch(cross)

        
        
def checkIfLevelFailed():
    print("Checking if the level was failed")
    if exists(Template(r"tpl1590451930540.png", record_pos=(0.001, -0.442), resolution=(1080, 1920))):
        touch(Template(r"tpl1590451943509.png", record_pos=(-0.006, -0.188), resolution=(1080, 1920)))


def checkIfLevelPassed():
    next = exists(Template(r"tpl1590525358296.png", record_pos=(0.003, 0.234), resolution=(1080, 1920)))
    
    if next:
        touch(next)

def checkIfPlayable():
    print("check if the game is playable or not")
    if exists(Template(r"tpl1589591684039.png", record_pos=(0.437, -0.817), resolution=(1080, 1920))):
        print("game is playable!!!")
        swipeDown()
        checkIfPlayable()
    else:
        checkForAds()
        checkIfLevelPassed()
        checkIfLevelFailed()
        checkIfPlayable()



# checkForAds()
checkIfPlayable()
# swipeDown()

# checkIfLevelFailed()





# print(cross)

# print(assertion)

# Next level exists, then tap that.
# next level button
# nextLevel = exists(Template(r"tpl1589586206874.png", record_pos=(-0.002, 0.237), resolution=(1080, 1920)))

# if nextLevel:
#     touch(Template(r"tpl1589586261670.png", record_pos=(-0.065, 0.217), resolution=(1080, 1920)))
#     #Go through playing the game again?

    





# text("5872080336")


# uninstall(apkFolderName + apkFileName)
        
# swipe([600,2000], [600, 0])

# print(exists(Template(r"tpl1589585728284.png", record_pos=(-0.406, -0.794), resolution=(1080, 1920))))


# checkForAds()
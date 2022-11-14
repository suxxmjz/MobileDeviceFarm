# -*- encoding=utf8 -*-
__author__ = "munib"

from airtest.core.api import *
from airtest.core.android.adb import ADB
from airtest.core.android.android import Android
import os
import sys
import pathlib

connect_device("Android:///")

dev = device()
print(dev)

print('Python Version')
print(sys.version)


# apkFolderName = 'apk/'
# apkFileName = 'com.google.android.youtube_v14.43.55-1443552000_Android-4.4.apk'
packageName = 'com.google.android.youtube'

# # install(apkFolderName + apkFileName)
start_app(packageName)


# # assert_exists(Template("tpl1588638442146.png"), "Please fill in the test point.")

# searchIconTemplate = Template(r"tpl1588639857277.png", threshold=1.0, record_pos=(0.288, -0.749), resolution=(1080, 1920))
# foodQuery = 'asmr chicken wings'

adb = ADB("R58N33813BE")
print(adb)

print(adb.version())
print(adb.devices())
# print(adb.sdk_version())

android = Android()

print(android.get_default_device())
print(android.list_app())

devices = [tmp[0] for tmp in ADB().devices()]

print(devices)

connect_device("Android:///" + "R58N33813BE")
start_app(packageName)

dev = device()

def swipeUp():
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
     swipe([600,2000], [600, 0])
    
def captureAd():
    sleep(1)
    epoch_time = int(time.time())
    dev.snapshot(filename= 'ads/' + str(epoch_time) + '.png')

    
def checkAds():
    adLogo = exists(Template(r"tpl1592938751365.png", record_pos=(-0.309, -0.148), resolution=(1080, 2400)))
    
    if adLogo:
        captureAd()
    
    swipeUp()
    checkAds()


checkAds()
# adb.shell("screenrecord --verbose --time-limit 30 /sdcard/demo.mp4")
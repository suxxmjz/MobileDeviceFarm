# -*- encoding=utf8 -*-

__author__ = "munib"

from airtest.core.api import *
import os
import sys
import pathlib

#### TODOS
## Todos go here


# You can specify to connect to a specific device, or create an adb bridge with a random device. using dev = device() method call.
connect_device("Android:///" + "RNV0216C14000113")

print('Python Version')
print(sys.version)

apkFolderName = 'apk/' ## Doesn't change unless you move the apk elsewhere
apkFileName = 'yourapp.apk'
packageName = 'com.yourapp.android.etc.etc'

def installApp():
    install(apkFolderName + apkFileName)
    start_app(packageName)

def checkForAd():

    ## Implement ad specific triggers here.
    result =  exists(Template(r"tpl1595360584308.png", record_pos=(-0.321, 0.246), resolution=(1080, 2400)))

    if type(result) is bool:
        print('Not an ad.')
    else:
        time.sleep(1)
        epoch_time = int(time.time())
        dev = device()
        dev.snapshot(filename= 'ads/' + str(epoch_time) + '.jpg')
        print("Saved ad")

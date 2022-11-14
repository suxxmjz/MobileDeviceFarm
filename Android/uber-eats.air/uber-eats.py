__author__ = "munib"

from airtest.core.api import *

auto_setup(__file__)

# -*- encoding=utf8 -*-
__author__ = "munib"

from airtest.core.api import *
import os
import sys
import pathlib


init_device("Android")

print('Python Version')
print(sys.version)

# pathToFile = '/ads'

# pathlib.Path('/my/directory').mkdir(parents=True, exist_ok=True)

# print(device())

# dev = device()
# dev.snapshot(filename='ads/xxx.png')

# def adjustAd():

#     if type(result) is bool:
#         print(result)
#         print('Not an ad.')
#     else:
#         (x, y) = result
#         print(x)
#         print(y)
#         swipeUp = swipe([x,y], [x, 300])

# while(1):


#     if type(result) is bool:
#         print(result)
#         print('Not an ad.')
#     else:
#         (x, y) = result
#         print(x)
#         print(y)
#         swipeUp = swipe([x,y], [x, 300])
#         adjustAd()
#         print('***swiped up')
#         print(swipeUp)
#         time.sleep(1)
#         epoch_time = int(time.time())
# #         os.makedirs(pathToFile, exist_ok=True)  
# #         snap = snapshot(filename= 'ad-' + str(epoch_time) + '.png')
#         dev = device()
#         dev.snapshot(filename= 'ads/' + str(epoch_time) + '.png')
#         print("Saved ad")

apkFolderName = 'apk/'
apkFileName = 'com.ubercab.eats_v1.210.10004-4837_Android-5.0.apk'
packageName = 'com.ubercab.eats'

# install(apkFolderName + apkFileName)
# start_app(packageName)
# # sleep(5.0)

# touch(Template(r"tpl1588636869899.png", record_pos=(0.003, 0.577), resolution=(1080, 1920)))
text("5872080336")


uninstall(apkFolderName + apkFileName)
        
# swipe([600,2000], [600, 0])
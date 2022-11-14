# -*- encoding=utf8 -*-
__author__ = "munib"

from airtest.core.api import *

init_device("Android")
# assert_exists(Template(r"tpl1587598382924.png", record_pos=(-0.243, -0.416), resolution=(1080, 1920)), "This is an ad.")

# print("HELLO")
# snap = snapshot(filename="hello.png", msg="Please fill in the test point.")
# print(snap)

connect_device("Android:///" + "RNV0216C14000113")


while(1):
    result = exists(Template(r"tpl1587780179450.png", record_pos=(-0.013, -0.108), resolution=(1080, 1920)))




    if type(result) is bool:
        print(result)
    else:
        (x, y) = result
        print(x)
        print(y)
        touch([x, y])
        time.sleep(1)
        swipe([600,1000], [600, 900])
#         epoch_time = int(time.time())
#         snap = snapshot(filename=  str(epoch_time) + '.png')
        
#     swipe([600,2000], [600,

# while(1):
#     result = exists(Template(r"tpl1587756402786.png", record_pos=(-0.264, -0.382), resolution=(1080, 1920)))

#     if type(result) is bool:
#         print(result)
#     else:
#         (x, y) = result
#         print(x)
#         print(y)
#         swipe([x,y], [x, 300])
#         epoch_time = int(time.time())
#         snap = snapshot(filename=  str(epoch_time) + '.png')
        
#     swipe([600,2000], [600, 0])

# adCheck = exists(Template(r"tpl1587674821148.png", record_pos=(-0.248, -0.316), resolution=(1080, 1920)))
# print(adCheck)
# if(adCheck):
#     print(adCheck)
#     print("ad exists!!!!!!!!!!!")
#     snapshot(filename='../ads/asd.png')
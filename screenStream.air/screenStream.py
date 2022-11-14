# -*- encoding=utf8 -*-

__author__ = "Sukriti"

from airtest.core.api import *



apkFolderName = 'apk/' ## Doesn't change unless you move the apk elsewhere
apkFileName = 'screenStream.air/screenstream.apk'
packageName = 'info.dvkr.screenstream'


def startApp():
        try:
                install(apkFileName)
        except:
                pass

        start_app(packageName)
        time.sleep(2)
        result = exists((Template(r"logo.jpg",resolution=(1080, 2400))))
        if type(result) is bool:
                print('Already started.')
        else:
                touch(result)
                time.sleep(2)
                result2 = exists((Template(r"startnow.jpg",resolution=(1080, 2400))))
                if type(result2) is bool:
                        print('Already started.')

                else:
                        touch(result)

startApp()
# -*- encoding=utf8 -*-

import os
from airtest.core.api import *
import subprocess
import psutil
import logging
import streamlit.logger



class Manager:
    """
    A class to instantiate a process run from script.

    ...
    Attributes
    ----------
    __scriptName : str
        name of the script to be run
    __deviceID : str
       device to be used
    __pathToAPK : str
        location of APK on computer
    __packageName : str
        package name of APK
    __pid : str
        unique ID for each process
    __screenRecord : bool
        option to record device and save video

    Methods
    --------
    """
    
    __pid : str = None
    __scriptName : str = None
    __deviceID : str = None
    __pathToAPK : str = None
    __packageName : str = None
    __sessionID : str = None
    __dev = None
    __screenRecord : bool = None
    logger = logging.getLogger()



    def __init__(self,scriptName: str, deviceID: str, pathToAPK: str, packageName : str, sessionID : str, screenRecord : bool) -> None:
        '''
        Constructor to set up an instance for each process.

            Parameters:
                scriptName (str): name of script
                deviceID (str) : device to be used
                pathToAPK(str) : path of APK on computer
                packageName(str) : name of package
                sessionID(str) : session ID
                screenRecord(bool) : screen record device
        '''
        self.__scriptName = scriptName
        self.__deviceID = deviceID
        self.__pathToAPK = pathToAPK
        self.__packageName = packageName
        self.__sessionID = sessionID
        self.__screenRecord = screenRecord
        streamlit.logger.get_logger = logging.getLogger
        streamlit.logger.setup_formatter = None
        streamlit.logger.update_formatter = lambda *a, **k: None
        streamlit.logger.set_log_level = lambda *a, **k: None
        try:
            os.mkdir('log')
            print('Logs folder made')
        except:
            print('Logs folder exists.')
        try:
            os.mkdir('log/' + self.__sessionID)
            print('Subfolder made')
        except:
            print('Subfolder ' + self.__sessionID +  ' already exists.')

       
        filePath = 'log/' + self.__sessionID +'/'+ 'ManagerLog_'+ self.__sessionID + '.txt'
        logging.basicConfig(filename = filePath, format = "%(asctime)s %(levelname)s:%(name)s:%(message)s", level = logging.DEBUG, force = True)
        logging.getLogger().addHandler(logging.StreamHandler())
        logging.info('Script: '+scriptName + ' Device: '+ deviceID + ' APK: ' + pathToAPK + " Session ID: " + sessionID)
        HTTPcmd = 'airtest run screenStream.air --device Android:///' +self.__deviceID
        subprocess.Popen(HTTPcmd, shell = True)
        time.sleep(20)
        

    def checkInputs(self) -> None:

        '''
        Sanitize user inputs. Will make sure each input is vaild
        or the program will exit with an error message.
        '''

        if not os.path.exists(self.__pathToAPK):
            logging.error("Path to APK doesn't exist or is incorrect.")
            exit(1)

        if not os.path.exists(self.__scriptName):
            logging.error("Script name is incorrect or it doesn't exist.")
            exit(1)
            
        self.connectDev()

    def connectDev(self) -> None:
        '''
        Connect android device using ADB.
        '''
        try:
            dev = connect_device("Android:///" + self.__deviceID)
            self.__dev = dev
            
            logging.info("Device " + self.__deviceID + " connected.")
        except:
            logging.error("Device is not connected or device ID is incorrect for " + self.__deviceID)
            exit(1)
        if self.__screenRecord == True:
            self.__dev.start_recording()

    def installAPK(self) -> None:
        '''
        Install APK on connected device. If already installed,
        the app will launch as normal and a message will be shown.
        '''
        try:
            install(self.__pathToAPK)
            logging.info("APK installed on " + self.__deviceID)
        except:
            logging.info("APK already installed on " + self.__deviceID)
        start_app(self.__packageName)

    def runScript(self) -> str:
        '''
        Will run the specified script by opening a subprocess. Returns process ID in
        form of a string.
        '''
        cmd = 'airtest run '+ self.__scriptName+ ' --device Android:///' +self.__deviceID + " --log log/" + self.__sessionID
        proc = subprocess.Popen(cmd, shell = True)
        logging.info("Script running on " + self.__deviceID)
        self.__pid = proc.pid
        return proc.pid

    def kill(self) -> None:
        '''
        Kills the specified process using its PID. If PID doesn't 
        exist or process is already killed, it will show a message.
        '''
        if (self.__pid != None):
            process = psutil.Process(self.__pid)
            for proc in process.children(recursive = True):
                proc.kill()
            process.kill()
            logging.info("Process " + str(self.__pid) + " killed on " + self.__deviceID)
        else:
            logging.error("PID not found or the process has already been killed on " + self.__deviceID)

    def uninstallAPK(self) -> None:
        '''
        Uninstalls APK from device. Is called after the script is done running.
        '''
        try:
            uninstall(self.__packageName)
            logging.info("APK uninstalled on " + self.__deviceID)
        except:
            logging.info("APK already uninstalled or package name is incorrect on " + self.__deviceID)

    def stopAPK(self) -> None:
        '''
        Stops app. Called after the script is done running.
        '''
        try:
            stop_app(self.__packageName)
            logging.info("Package " + self.__packageName + " stopped.")
        except: 
            logging.info("Package: " + self.__packageName + " already stopped.")
        if self.__screenRecord == True:
            self.__dev.stop_recording(output = 'log/' + self.__sessionID + "/" + self.__deviceID + '.mp4')
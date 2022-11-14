import streamlit as st
import runner
import os
import time
from zipfile import ZipFile




prog = runner.Runner()
def app():
    '''
    Gets input for session one at a time from the user. THE APK and ZIP folder are stored in a session folder.
    '''
    with st.form(key = "input_form", clear_on_submit= True):
        st.title('Input')
        st.write("Start a session here.")
        zippedScript = st.file_uploader("Upload ZIP Air Folder:")  #uplooaded air folder
        uploadedAPK = st.file_uploader("Upload APK:")  #uploaded apk
        pkg = st.text_input("Package:", type = "default") #package name
        numberOfDev = st.number_input("Number of devices:", min_value = 1, step = 1) #number of devices
        duration = st.number_input("Session Duration (in minutes):", min_value = 1.5, step = 0.5) #duration of session
        yesNo = ['No', 'Yes']
        recordOption = st.selectbox("Screen record devices:",yesNo, key = "yesNo" )  #option to screen record devices
        uninstallOption = st.selectbox("Uninstall APK after session:", yesNo, key = "uninstallOption") #option to uninstall apk after session
        submit_button = st.form_submit_button(label='Submit')

        
        if submit_button:
            zipExt = zippedScript.name[-4:]
            apkExt = uploadedAPK.name[-4:]
            if zipExt == ".zip":
                if apkExt == ".apk":
                    if pkg != "":
                        try:
                            os.mkdir("Sessions")
                        except:
                            pass

                        epochTime = str(int(time.time()))   #create the session ID
                        try:
                            filePath = "Sessions/" + epochTime  #file path to store session script and apk
                            os.mkdir(filePath)
                            
                        except:
                            pass
                        
                        APKPath = os.path.join(filePath, uploadedAPK.name) #path to APK

                        with open(os.path.join(filePath, uploadedAPK.name), "wb") as a:
                            a.write(uploadedAPK.getbuffer())

                        extractedFiles = ZipFile (zippedScript, 'r')  #extract the uploaded zip folder
                        extractedFiles.extractall(filePath)

                        unzippedFolder = zippedScript.name[:-4]

                        scriptFold = filePath + "/" + unzippedFolder #path to folder with script

                        uninstallAPKOption : bool = None
                        recordingOption : bool = None

                        if recordOption == "Yes":
                            recordingOption = True
                        if recordOption == "No":
                            recordingOption = False

                        if uninstallOption == "Yes":
                            uninstallAPKOption = True
                        if uninstallOption == "No":
                            uninstallAPKOption = False

                        duration = int(duration * 60)
                        
                        prog.takeInput(scriptFold,APKPath,pkg,numberOfDev, duration, epochTime, recordingOption, uninstallAPKOption)
                        st.success("Submitted successfully.")

                    else:
                        st.error("Something went wrong.")
                else:
                    st.error("File is not APK.")
            else:
                st.error("File is not ZIP file.")
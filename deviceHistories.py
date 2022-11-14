
import streamlit as st
import os


def app():
    '''
    View what apks each device has run.
    '''
    st.title("Device Histories")
    st.write("View individual device files to see which scripts they have run.")
    folder_path = 'DeviceHistory'

    filenames = os.listdir(folder_path)

    getFile = st.selectbox('Select a file', (filenames), key = 'historykey')
    openFile(getFile)

def openFile(getFile : str):
    '''
    Open the text file for the specified device.

    Parameters:
        getFile(str) : file to open
    '''
    filename = os.path.join('DeviceHistory', getFile)
    col1,col2, col3, col4, col5, col6= st.columns(6)
    try:
        with open(filename) as theFile:
            st.text(theFile.read())
            if os.stat(filename).st_size == 0:
                st.info(filename + " is empty")
            else:
                with col6:
                    clear = st.button('Clear File')
                if clear:
                    try:
                        open(filename, 'w').close()
                        st.success("File cleared")
                    except:
                        st.error("File could not be cleared")
    except FileNotFoundError:
        
        st.error('File not found.')
    with col1:
        refButton = st.button("Refresh", key = "deviceHistoryRefresh")

    if refButton:
        st.experimental_rerun()
           
    
   


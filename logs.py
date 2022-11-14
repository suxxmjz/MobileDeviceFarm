import streamlit as st
import glob, os
from PIL import Image
import shutil
import itertools

def app():
    '''
    This is the page where the user can view the contents of a log file.
    The user must input the session ID and the package name, then they can use the
    selectbox to perform various actions.
    
    '''
    st.title("Session Logs")
    st.write("View session log files.")
    with st.form(key = "log_form"):
        getID = st.text_input("Enter session ID")  #session ID
        folderName = "log/" + getID #log folder for session
        sessionFolder = "Sessions/" + getID #session folder(where uploaded files are stores - the air folder and the apk)
        option_names = ['View Manager Log Text File','View Airtest Log File', 'View Log Screenshots', 'View Device Videos', 'Delete Log Folder', 'Delete Session Folder']
        option = st.selectbox('What would you like to do?',option_names,  key = "logkey")
        isExist = os.path.isdir(folderName) #check if log folder exists
        sessionExist = os.path.isdir(sessionFolder) #check if session folder exists
        contButton = st.form_submit_button(label='Continue')

        if contButton:

            if option == 'Delete Session Folder':
                if sessionExist == True:
                    try:
                        shutil.rmtree(sessionFolder)
                    except: 
                        pass
                    try:
                        os.rmdir(sessionFolder)
                    except:
                        pass
                    st.success("Session folder deleted.")
                else:
                    st.error("Session folder not found.")

            
            if option == 'View Manager Log Text File':
                if isExist == True:
                    fileName = folderName + '/ManagerLog_' + getID + ".txt"
                    try:
                        with open(fileName) as theFile:
                            st.text(theFile.read())
                    except FileNotFoundError:
                        st.error('File not found.')
                if isExist == False:
                    st.error("Log folder not found.")

            if option == 'View Airtest Log File':
                if isExist == True:
                    logFile = folderName + '/log.txt'
                    try:
                        with open(logFile) as logF:
                            st.text(logF.read())
                    except FileNotFoundError:
                        st.error('File not found.')
                if isExist == False:
                    st.error("Log folder not found.")
                
            if option == 'View Log Screenshots':
                if isExist == True:
                    numImages = st.number_input("How many images per page? (press continue after each selection)", min_value = 5, step = 1)
                    if numImages > 4:
                        demonstrate_image_pagination(folderName, numImages)
                if isExist == False:
                    st.error("Log folder not found.")

            if option == 'View Device Videos':
                if isExist == True:
                    vidFile = None
                    for file in glob.glob(folderName +'/' + "*.mp4"):
                        vidFile = open(file, 'rb')
                        vidBytes = vidFile.read()  
                        st.video(vidBytes)
                        st.caption(file)
                    if vidFile == None:
                        st.error("No videos found.")
                if isExist == False:
                    st.error("Log folder not found.")

            if option == 'Delete Log Folder':
                if isExist == True:
                    try:
                        shutil.rmtree(folderName)
                    except: 
                        pass
                    try:
                        os.rmdir(folderName)
                    except:
                        pass
                    st.success("Log folder deleted.")
                if isExist == False:
                    st.error("Log folder not found.")
            


def paginator(label : str, items, numImages : int):
    '''
    Lets the user paginate a set of items.

    Parameters:
        label(str) : The label to display over the pagination widget.
        items(Iterator[Any]) : The items to display in the paginator.
        items_per_page(int) : The number of items to display per page.
        
    '''
   
    location = st.empty()

    # Display a pagination selectbox 
    items = list(items)
    n_pages = len(items)
    n_pages = (len(items) - 1) // numImages + 1
    page_format_func = lambda i: "Page %s" % i
    page_number = location.selectbox(label, range(1, int(n_pages + 1)), format_func=page_format_func)

    # Iterate over the items in the page to let the user display them.
    min_index = int(page_number - 1) * numImages
    max_index = min_index + numImages
    return itertools.islice(enumerate(items), min_index, max_index)

def demonstrate_image_pagination(folderName : str, numImages : int):
    images = []
    for file in glob.glob(folderName +'/' + "*.jpg"):
        img = Image.open(file)
        images.append(img)
    if images:
        image_iterator = paginator("Select a page (press continue after each selection)", images, numImages)
        indices_on_page, images_on_page = map(list, zip(*image_iterator))
        st.image(images_on_page, width=220)
    else:
        st.error("No images found")


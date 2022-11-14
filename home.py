import streamlit as st

def app():
    '''
    This is the entry point into the server for the user. It displays a summary of the pages.
    '''
    st.title('Home')

    st.write('This is the `home page` of the mobile device farm. View the summaries of each page below.')
    st.write('`Input`: Upload zip airtest folder, APK and specify session duration and number of devices.')
    st.write('`Device Statuses`: View table of devices in the farm and see their availablity, view live stream of each device using their IP addresses.')
    st.write('`Session Queue`: View the statuses of each session.')
    st.write('`Device Histories`: View files of what apps each device has run.')
    st.write('`Session Logs`: View files, images and videos of sessions.')


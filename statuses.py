import streamlit as st
import pandas as pd
import webbrowser


def app():
    '''
    Displays the excel dataframe of device statuses and IP addresses. The IP address can then be used to
    watch a live screen stream of the chosen device.
    '''
    st.title('Device Statuses')

    st.write("This page displays the `status` of each device connected.")
    
    df = pd.read_excel("devices.xlsx")

    st.dataframe(df)

    refButton = st.button("Refresh")

    if refButton:
        st.experimental_rerun()

    st.subheader("View Device Screen")
    with st.form(key = "screenForm", clear_on_submit= True):
        inputIP = st.text_input("Input device IP address (refer to table above):")
        viewButton = st.form_submit_button(label='View')
    
    if viewButton:
        url = "http://" + inputIP + ":8080"
        webbrowser.open(url)
        st.info("External tab has been opened.") 
    



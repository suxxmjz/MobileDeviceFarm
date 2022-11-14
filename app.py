import streamlit as st
from multiapp import MultiApp
import home, statuses, getInput, sessionQueue,deviceHistories, logs # import your app modules here

text_input_container = st.empty()
textCont = st.empty()

setUser = "DIHUSER"
setPass = "DIHPASS"
user = text_input_container.text_input("User", type = "default")
password = textCont.text_input("Password", type = "password")


if setUser == user and password == setPass:
    textCont.empty()
    text_input_container.empty()
        
    app = MultiApp()
        # Add all your application here
    try:
        app.add_app("Home", home.app)
        app.add_app("Input", getInput.app)
        app.add_app("Device Statuses", statuses.app)
        app.add_app("Session Queue", sessionQueue.app)
        app.add_app("Device Histories", deviceHistories.app)
        app.add_app("Session Logs",logs.app)
        #app.add_app("View Screen", viewScreen.app)
    except ValueError:
        pass
        # The main app
    app.run()
else:
    if user == "" or password =="":
        pass
    else:
        st.warning("Login invalid.")
    
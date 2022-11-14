import streamlit as st

def app():
    '''
    This page displays the queues, which are read from 3 text files(updated by the runner).
    '''
    st.title('Session Queue')

    st.write("This page displays the `status` of each session (waiting in queue, running or completed).")

    selected = st.radio("What would you like to view?",('Sessions waiting in queue','Active Sessions', 
    'Completed Sessions'))
    
    if selected == 'Sessions waiting in queue':
        st.subheader("Sessions Waiting in Queue")
        filename = 'inQueue.txt'
        try:
            with open(filename) as theFile:
                st.text(theFile.read())
        except FileNotFoundError:
            st.error('File not found.')
    
    if selected == 'Active Sessions':
        st.subheader('Active Sessions')
        filename = 'activeSessions.txt'
        try:
            with open(filename) as theFile:
                st.text(theFile.read())
        except FileNotFoundError:
            
            st.error('File not found.')
    
    if selected == 'Completed Sessions':
        st.subheader('Completed Sessions')
        filename = 'completedSessions.txt'
        try:
            with open(filename) as theFile:
                st.text(theFile.read())
        except FileNotFoundError:
            
            st.error('File not found.')
    

    refButton = st.button("Refresh", key = "sessionQueueRefresh")

    if refButton:
        st.experimental_rerun()
    
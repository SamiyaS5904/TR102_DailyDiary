# AGENTIC AI START 

# Chatbots with Streamlit UI
# when you make something using chatgpt (it's not an AI Agent)  ----> it is simple gen ai

""" 
For an agent : 
            -> interface (ui)
            -> database
            -> goal ----
            -> task
        
    AGENTIC AI
        -> CONTROLLER:
                AI Model, Goal and Task

        -> VIEW:
                Streamlit Chat UI

        -> MODEL:
                Dictionary (Agentic AI with Python)                         

"""

import streamlit as st
st.set_page_config(page_title='Chat UI')
st.title('Chat UI Demo')

st.subheader('Ask a question, i will help you with answer')

# if you have to give question answers in dictionary (question will be key , ans will be value)


# Here the question bank is static it cannot Shrink or Grow
# If you want dyanamic -- > use MongoDB

question_bank = {
    'what is python' : 'it is a programming language',
    'can i build an ai agent' : 'yes you can using Python, OpenAI, CrewAI and many more',
    'what is streamit' : 'it is a UI Library'
} 

message = {
    'role':'User',
    'content': 'what is python',
}

message = {
    'role':'Agent',
    'content': 'what is python',
}


# Create an empty list inside the session state of streamlit
# Session State is object's Reference which will store data temporarily


if 'messages' not in session_state:
    st.session_state.messages = []

    


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
message = {
    'role': 'user',
    'content': 'what is python'
    }

    message = {
        'role': 'agent',
        'content': 'its a programming language'
    }
"""
for message in st.session_state.messages:
    if message['role'] == 'user':    
        with st.chat_message(message['role']):
            st.markdown(message['content'])
    else:
        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)

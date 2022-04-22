import streamlit as st
import speech_recognition as sr

st.title('Speechtrum | Tugas Besar Speech Processing')

# if 'run' not in st.session_state:
#     st.session_state['run'] = False

# def start_listening():
#     st.session_state['run'] = True

# def stop_listening():
#     st.session_state['run'] = False

# start,stop = st.columns(2)

# start.button('Start listening', on_click = start_listening())

# start.button('Stop listening', on_click = stop_listening())

listening = True

def listening():
    recognizer = sr.Recognizer()

    while listening:

        try:

            with sr.Microphone() as mic:
                
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio, language = 'id-ID')

                print(f"Recognizeed {text}")
                st.write(f"{text.lower()}")
            
        except sr.UnknownValueError:

            recognizer = sr.Recognizer()
            print(".")
            continue

if st.checkbox('Toggle Listen'):
    st.subheader('Say something ... 🎤')
    listening()
else:
    st.subheader('We are deaf now ... 🍻')
    listening = False

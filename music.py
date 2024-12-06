import streamlit as st
import webbrowser
lang =st.text_input("Language")
mood =st.text_input("Mood")
btn= st.button("Recommend me song")
if btn:
    webbrowser.open(f"https://www.google.com/search?q={mood}+{lang}+songs+spotify&rlz=1C1VDKB_enIN1030IN1030&oq=happy+english+songs&gs_lcrp=EgZjaHJvbWUqBggAEEUYOzIGCAAQRRg7MgkIARBFGDkYgAQyBwgCEAAYgAQyBggDEEUYQDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIGCAcQRRg80gEJMTUwMzZqMGo3qAIIsAIB&sourceid=chrome&ie=UTF-8")
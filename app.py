import streamlit as st
import whisper
import tempfile
import os

from llm.groq_llm import ask_groq
from tts.elevenlabs_tts import text_to_speech

st.set_page_config(page_title="🎙️ Voice AI Agent")
st.title("🎙️ Real-Time Voice AI Agent")

st.write("👇 Record your voice (timer WILL run)")

audio = st.audio_input("🎤 Record here")

if audio:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as f:
        f.write(audio.read())
        audio_path = f.name

    st.success("✅ Audio recorded")

    
    with st.spinner("Transcribing..."):
        model = whisper.load_model("base")
        result = model.transcribe(audio_path)
        text = result["text"]

    st.subheader("📝 You said:")
    st.write(text)


    with st.spinner("Thinking..."):
        reply = ask_groq(text)

    st.subheader("🤖 AI Response:")
    st.write(reply)

    with st.spinner("Speaking..."):
        speech = text_to_speech(reply)

    st.audio(speech)

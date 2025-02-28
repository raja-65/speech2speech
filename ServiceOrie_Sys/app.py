import streamlit as st
from audiorecorder import audiorecorder
import io
import os
import tempfile
from dotenv import load_dotenv
from groq import Groq  # Install via 'pip install groq'
from elevenlabs.client import ElevenLabs
from elevenlabs import play

# Load API keys
load_dotenv()

# Initialize API clients
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
eleven_client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

# Streamlit UI
st.title("🎙️ Real-Time Hindi Voice Conversational AI")
st.write(
    "Speak in Hindi. Your voice is transcribed, translated, processed by an AI, translated back to Hindi, and converted to speech."
)

st.markdown("### 🎤 Record Your Voice")
audio = audiorecorder("Click to record", "Click to stop recording")

if len(audio) > 0:
    st.audio(audio.export().read(), format="audio/wav")  # Play recorded audio

    # Save audio as a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        tmpfile.write(audio.export().read())
        tmpfile.flush()
        audio_filepath = tmpfile.name

    # Step 1: Transcribe & Translate (Hindi → English)
    with st.spinner("📝 Transcribing & Translating..."):
        try:
            transcript = groq_client.audio.translations.create(
                file=(
                    os.path.basename(audio_filepath),
                    open(audio_filepath, "rb").read(),
                ),
                model="whisper-large-v3",
                prompt="Translate Hindi speech to English text.",
                response_format="json",
                temperature=0.0,
            )
            english_text = transcript.text
            st.markdown("**🔹 Translated English Text:**")
            st.write(english_text)
        except Exception as e:
            st.error(f"❌ Transcription Error: {e}")
            st.stop()

    # Step 2: Generate AI Response
    with st.spinner("🤖 Generating AI Response..."):
        try:
            chat_response = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a helpful AI."},
                    {"role": "user", "content": english_text},
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.5,
                max_completion_tokens=1024,
                top_p=1,
            )
            english_response = chat_response.choices[0].message.content
            st.markdown("**🔹 AI Response (English):**")
            st.write(english_response)
        except Exception as e:
            st.error(f"❌ AI Error: {e}")
            st.stop()

    # Step 3: Translate AI Response to Hindi
    with st.spinner("🌎 Translating AI Response to Hindi..."):
        try:
            translation_response = groq_client.chat.completions.create(
                messages=[
                    {"role": "system", "content": "You are a translator."},
                    {
                        "role": "user",
                        "content": f"Translate to Hindi: {english_response}",
                    },
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.5,
                max_completion_tokens=1024,
                top_p=1,
            )
            hindi_response = translation_response.choices[0].message.content
            st.markdown("**🔹 AI Response (Hindi):**")
            st.write(hindi_response)
        except Exception as e:
            st.error(f"❌ Translation Error: {e}")
            st.stop()

    # Step 4: Convert Hindi Text to Speech
    with st.spinner("🔊 Generating Voice Response..."):
        try:
            # Generate TTS audio (returns a generator of bytes)
            tts_audio_generator = eleven_client.text_to_speech.convert(
            text=hindi_response,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        # Convert generator to a byte stream
            tts_audio_bytes = b"".join(tts_audio_generator)

        # Stream the audio in Streamlit
            st.markdown("**🎧 AI Voice Response:**")
            st.audio(tts_audio_bytes, format="audio/mp3")

        # Instead of saving to a file and passing a filename,
        # pass the bytes directly to the play() function.
            play(tts_audio_bytes)

        except Exception as e:
            st.error(f"❌ Speech Synthesis Error: {e}")

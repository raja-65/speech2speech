# speech2speech
s2s with groq and 11labs API key

# 🎙️ Voice-to-Voice Conversational AI (Hindi ↔ English)

## 📌 Overview

This project enables real-time voice-based conversations in Hindi using AI-powered speech recognition, translation, and text-to-speech synthesis. The workflow is as follows:

1. **Voice Input:** The user records speech in Hindi.
2. **Speech-to-Text:** Groq's Whisper model transcribes the speech into text.
3. **Translation:** The Hindi text is translated into English.
4. **AI Response:** A response is generated using the Llama 3.3-70B model.
5. **Translation Back to Hindi:** The AI-generated English response is translated into Hindi.
6. **Text-to-Speech:** The translated Hindi response is converted into speech using ElevenLabs API.
7. **Voice Output:** The AI-generated voice response is played back to the user.

## 🚀 Installation Guide

### **Prerequisites**
- **Python 3.8+**
- **API keys** for:
  - **Groq API** (for speech-to-text and AI responses) → [Get it here](https://groq.com/)
  - **ElevenLabs API** (for text-to-speech) → [Get it here](https://elevenlabs.io/)
- **Internet Connection** for API calls

### **Setup Instructions**
1. **Clone the repository:**
   ```bash
   git clone https://github.com/raja-65/speech2speech.git
   cd ServiceOrie_sys

Install dependencies:

pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project folder.
Add the following keys inside .env:

GROQ_API_KEY=your_groq_api_key_here
ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
Replace your_groq_api_key_here and your_elevenlabs_api_key_here with your actual API keys.
---- add existing env file inside serviceorie_sys folder and update with api keys instructions in env.txt----------------

# Run the application

streamlit run app.py

🎥 Demo
A demo video has been uploaded to GitHub. Watch it to see how the system works.

⚠️ Important Note
This is the final submission of the project, not just the first iteration. All required functionalities have been implemented.


📩 Contact
For any queries, reach out cse210001056@iiti.ac.in

---

### **What This README Covers**
✅ Simple and clear instructions for users  
✅ Ensures `.env` file is stored inside the project folder  
✅ Provides API links for users to get their keys  
✅ Informs the Teaching Assistant (TA) that this is the **final submission**  
✅ Includes a section for a **demo video**  

Let me know if you need any edits! 🚀


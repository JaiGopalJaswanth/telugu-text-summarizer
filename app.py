import streamlit as st
from deep_translator import GoogleTranslator
from transformers import pipeline

# App Title
st.set_page_config(page_title="Telugu Text Summarizer")
st.title("🧠 Telugu Text to English Summary")
st.caption("An AI tool that summarizes Telugu text into English — built for Vishwam.ai Internship 🚀")

# Input box
telugu_input = st.text_area("✍️ Enter Telugu text here:", height=200, placeholder="ఇక్కడ మీ తెలుగు వాక్యాన్ని టైప్ చేయండి...")

if st.button("🧠 Summarize"):
    if not telugu_input.strip():
        st.warning("Please enter some Telugu text.")
    else:
        with st.spinner("🔄 Translating and summarizing..."):
            # Translate Telugu → English
            try:
                english_text = GoogleTranslator(source='te', target='en').translate(telugu_input)
            except Exception as e:
                st.error(f"Translation failed: {str(e)}")
                st.stop()

            # Summarize English
            try:
                summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
                summary = summarizer(english_text, max_length=60, min_length=10, do_sample=False)[0]['summary_text']
            except Exception as e:
                st.error(f"Summarization failed: {str(e)}")
                st.stop()

        # Output
        st.subheader("🌍 English Translation")
        st.write(english_text)

        st.subheader("📝 English Summary")
        st.success(summary)

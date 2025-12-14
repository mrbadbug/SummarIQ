import streamlit as st
from summarizer import summarize_text

st.set_page_config(page_title="SummarIQ", layout="centered")

st.title("🧠 SummarIQ - Intelligent Text Summarization")

text = st.text_area("Enter text to summarize", height=300)

if st.button("Generate Summary"):
    if text.strip():
        summary = summarize_text(text)
        st.subheader("📄 Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text.")

import streamlit as st
from summarizer import summarize_text

st.set_page_config(
    page_title="SummarIQ",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>
.stButton>button {
    background: #0F3479E4;
    border-radius: 10px;
    font-weight: 600;
}
.main-title {
    font-size: 40px;
    font-weight: 800;
    background-color: #0F3479E4;
    border-radius: 20px;
    padding-top: 0px;
}
</style>
""", unsafe_allow_html=True)
st.sidebar.header("SUMMARIQ")
st.sidebar.divider()
st.sidebar.header("Let you know the summary of the text.")
st.sidebar.divider()
st.sidebar.markdown("""
**Please be patient**
- More features will be added soon
                    
**Developed by**
- Zakir Hussain Monir
- Daffodil International University
""")

st.markdown("<div class='main-title'>🧠 SummarIQ - Intelligent Text Summarizer</div>", unsafe_allow_html=True)
st.caption("Powered by BART Transformer Model, HuggingFace Dataset.")
st.divider()
text = st.text_area("Enter text to summarize", height=300)
if st.button("Generate Summary"):
    if text.strip():
        summary = summarize_text(text)
        st.subheader("📄 Summary")
        st.write(summary)
    else:
        st.warning("Please enter some text.")

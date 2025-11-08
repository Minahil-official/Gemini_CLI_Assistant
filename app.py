import streamlit as st

st.set_page_config(
    page_title="Content-Pro",
    page_icon="📝",
    layout="wide"
)

st.title("Welcome to Content-Pro! 👋")
st.write("---")

st.markdown("""
**Content-Pro** is your go-to application for all your content needs. Whether you want to summarize a lengthy document, simplify complex text, or create a quiz to test your knowledge, Content-Pro has got you covered.

### Features:
- **Summarizer**: Get a concise summary of your text.
- **Simplifier**: Rewrite your text in simple and easy-to-understand language.
- **Quiz Generator**: Create a multiple-choice quiz from your text.

Navigate to the desired page from the sidebar to get started.
""")

st.info("Select a page from the sidebar to begin.")

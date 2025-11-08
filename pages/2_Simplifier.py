import streamlit as st

st.set_page_config(
    page_title="Simplifier",
    page_icon="🗣️",
    layout="wide"
)

st.title("🗣️ Simplifier")
st.write("---")

st.markdown("### Paste your text below to get a simplified version.")

input_text = st.text_area("Enter your text here:", height=200)

if st.button("Simplify"):
    if input_text:
        st.markdown("### Simplified Text:")
        # Placeholder for simplification logic
        simplified_text = "This is a simplified version of your text. The original text has been rewritten to be easier to understand."
        st.info(simplified_text)
    else:
        st.warning("Please enter some text to simplify.")

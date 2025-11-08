import streamlit as st

st.set_page_config(
    page_title="Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Summarizer")
st.write("---")

st.markdown("### Paste your text below to get a summary.")

input_text = st.text_area("Enter your text here:", height=200)

if st.button("Summarize"):
    if input_text:
        st.markdown("### Summary:")
        # Placeholder for summarization logic
        summary = " ".join(input_text.split()[:50]) + "..."
        st.success(summary)
    else:
        st.warning("Please enter some text to summarize.")

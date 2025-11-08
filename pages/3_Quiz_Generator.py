import streamlit as st
import re
import random

def generate_quiz_from_text(text):
    # Simple keyword extraction (most frequent words, excluding stop words)
    stop_words = set("a an the and is in on of to for with".split())
    words = re.findall(r'\b\w+\b', text.lower())
    words = [word for word in words if word not in stop_words and len(word) > 3]
    if not words:
        return None

    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort words by frequency
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    # Select top 3 keywords
    keywords = [word for word, freq in sorted_words[:3]]
    if not keywords:
        return None

    quiz = []
    sentences = text.split('.')
    
    for keyword in keywords:
        for sentence in sentences:
            if keyword in sentence.lower():
                question = sentence.replace(keyword, "______")
                
                # Generate options
                options = [keyword.capitalize()]
                other_words = [word for word in words if word != keyword]
                if len(other_words) < 3:
                    options.extend(other_words)
                else:
                    options.extend(random.sample(other_words, 3))
                
                random.shuffle(options)
                
                quiz.append({
                    "question": question,
                    "options": options,
                    "answer": keyword.capitalize(),
                    "explanation": f"The correct answer is {keyword.capitalize()}."
                })
                break # Move to the next keyword
    return quiz

st.set_page_config(
    page_title="Quiz Generator",
    page_icon="❓",
    layout="wide"
)

st.title("❓ Quiz Generator")
st.write("---")

st.markdown("### Paste your text below to generate a quiz.")

input_text = st.text_area("Enter your text here:", height=200, key="quiz_input")

if "quiz_generated" not in st.session_state:
    st.session_state.quiz_generated = False

if st.button("Generate Quiz"):
    if input_text:
        with st.spinner("Generating quiz..."):
            quiz = generate_quiz_from_text(input_text)
            if quiz:
                st.session_state.quiz = quiz
                st.session_state.quiz_generated = True
                st.session_state.user_answers = [None] * len(st.session_state.quiz)
            else:
                st.error("Could not generate a quiz from the provided text. Please try with a different text.")
    else:
        st.warning("Please enter some text to generate a quiz.")

if st.session_state.quiz_generated:
    st.markdown("### Generated Quiz:")
    for i, q in enumerate(st.session_state.quiz):
        st.subheader(f"Question {i+1}: {q['question']}")
        st.session_state.user_answers[i] = st.radio(f"Options for question {i+1}", q["options"], key=f"q{i}")

    st.write("---")
    if st.button("Show Result"):
        score = 0
        for i, q in enumerate(st.session_state.quiz):
            if st.session_state.user_answers[i] == q["answer"]:
                score += 1
        
        st.header("Quiz Results")
        st.write(f"You scored {score} out of {len(st.session_state.quiz)}.")

        for i, q in enumerate(st.session_state.quiz):
            st.subheader(f"Question {i+1}: {q['question']}")
            if st.session_state.user_answers[i] == q["answer"]:
                st.success(f"Your answer: {st.session_state.user_answers[i]} (Correct)")
            else:
                st.error(f"Your answer: {st.session_state.user_answers[i]} (Incorrect)")
                st.info(f"Correct answer: {q['answer']}")
            st.write(f"**Explanation:** {q['explanation']}")
            st.write("---")
        st.session_state.quiz_generated = False
import streamlit as st
from huggingface_hub import InferenceClient
import json

st.title("🗣️Smart MCQ Generator")

topic = st.text_input("Enter a topic", placeholder="Example: Python")

number = st.number_input(
    "Number of questions",
    min_value=1,
    max_value=10,
    value=5
)

if st.button("Generate MCQs"):

    if topic == "":
        st.warning("Please enter a topic.")
    else:
        client = InferenceClient(
            api_key=st.secrets["HF_TOKEN"]
        )

        prompt = f"""
Generate {number} multiple choice questions about {topic}.
Each question should have 4 options and one correct answer.
Return the questions in JSON format.
"""

        with st.spinner("Generating questions..."):

            response = client.chat.completions.create(
                model="openai/gpt-oss-120b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=2000
            )

        text = response.choices[0].message.content

        try:
            text = text.replace("```json", "").replace("```", "").strip()

            questions = json.loads(text)

            st.session_state.questions = questions
            st.session_state.submitted = False

        except:
            st.error("The AI did not return valid JSON.")
            st.write(text)


if "questions" in st.session_state:

    st.subheader("MCQ Quiz")

    answers = {}

    for i, q in enumerate(st.session_state.questions):

        st.write(f"### Question {i + 1}")
        st.write(q["question"])

        answers[i] = st.radio(
            "Choose your answer:",
            q["options"],
            key=f"question_{i}"
        )

    if st.button("Submit Quiz"):

        score = 0

        for i, q in enumerate(st.session_state.questions):

            if answers[i] == q["answer"]:
                score += 1

        st.success(
            f"Your score: {score}/{len(st.session_state.questions)}"
        )
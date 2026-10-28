
import os
import streamlit as st
from roadmap import generate_roadmap

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎯"
)

st.title("🎯 AI Learning Roadmap Generator")
st.write("Create your personalized learning plan with AI.")

field = st.text_input(
    "What do you want to learn?",
    placeholder="e.g. Cybersecurity, Python, AI"
)

level = st.selectbox(
    "Select your skill level",
    ["Beginner", "Intermediate", "Advanced"]
)

weeks = st.number_input(
    "Learning duration (weeks)",
    min_value=1,
    max_value=104,
    value=8
)

hours = st.number_input(
    "Available hours per week",
    min_value=1,
    max_value=80,
    value=5
)

if st.button("Generate My Roadmap"):

    if not field.strip():
        st.warning("Please enter a learning field.")

    elif not os.environ.get("GROQ_API_KEY"):
        st.error("Groq API key is missing.")

    else:
        try:
            with st.spinner("Generating your roadmap..."):
                result = generate_roadmap(
                    field, level, weeks, hours
                )

            st.success("Your roadmap is ready!")
            st.markdown(result)

            st.download_button(
                "Download Roadmap",
                data=result,
                file_name="learning_roadmap.md",
                mime="text/markdown"
            )

        except Exception as e:
            st.error(f"Error: {e}")

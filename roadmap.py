
import os
import streamlit as st

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎯",
    layout="centered"
)

st.title("🎯 AI Learning Roadmap Generator")
st.write("Create your personalized learning roadmap with AI.")

# User inputs
field = st.text_input(
    "What do you want to learn?",
    placeholder="e.g. Cybersecurity, Python, Artificial Intelligence"
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
    "Available study hours per week",
    min_value=1,
    max_value=80,
    value=5
)

# Generate roadmap
if st.button("Generate My Roadmap", type="primary"):

    if not field.strip():
        st.warning("Please enter a learning field.")

    elif not os.environ.get("GROQ_API_KEY"):
        st.error(
            "Groq API key is missing. "
            "Add GROQ_API_KEY in Streamlit Secrets."
        )

    else:
        try:
            from roadmap import generate_roadmap

            with st.spinner("Generating your roadmap..."):
                result = generate_roadmap(
                    field.strip(),
                    level,
                    int(weeks),
                    int(hours)
                )

            if result:
                st.success("Your roadmap is ready!")
                st.markdown(result)

                st.download_button(
                    label="Download Roadmap",
                    data=result,
                    file_name="learning_roadmap.md",
                    mime="text/markdown"
                )
            else:
                st.warning("The AI returned an empty roadmap.")

        except ModuleNotFoundError as e:
            if e.name == "roadmap":
                st.error(
                    "roadmap.py is missing. "
                    "Upload roadmap.py to the same GitHub "
                    "folder as app.py."
                )
            else:
                st.error(
                    f"Missing Python package: {e.name}. "
                    "Check requirements.txt."
                )

        except Exception as e:
            st.error(
                "Could not generate the roadmap. "
                "Check your API key, model availability, "
                "and Streamlit logs."
            )
            st.caption(f"Error type: {type(e).__name__}")

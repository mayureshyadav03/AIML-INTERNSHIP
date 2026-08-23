import time
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="🎓"
)

st.title("🎓 AI Study Assistant")
st.write("Learn any topic with the help of AI.")

topic = st.text_input(
    "Enter a topic you want to learn:",
    placeholder="Example: Machine Learning"
)

if st.button("Generate Study Material"):

    if not topic.strip():
        st.warning("Please enter a topic first.")

    else:
        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        prompt = f"""
        You are an AI Study Assistant.

        Help a BTech Artificial Intelligence and Machine Learning
        student understand the following topic:

        Topic: {topic}

        Provide the response in these sections:

        1. Simple Explanation
        2. Key Points
        3. Real-World Applications
        4. Important Terms
        5. Five Practice Questions
        6. Study Tips

        Keep the explanation beginner-friendly,
        accurate, and well structured.
        """

        with st.spinner("Generating study material..."):
            for attempt in range(3):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.7-flash",
                        contents=prompt
                    )
                    break

                except Exception:
                    if attempt < 2:
                        time.sleep(3)
                    else:
                        st.error(
                            "Gemini is temporarily unavailable. "
                            "Please try again in a few moments."
                        )
                        st.stop()

            st.subheader("📚 Study Material")
            st.markdown(response.text)
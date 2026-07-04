
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🤖",
    layout="wide"
)

with st.sidebar:
    st.title("🤖 AI Learning Buddy")
    st.write("Built by Preethi")
    st.markdown("---")
    st.write("### Activities")
    st.write("📖 Explain Concept")
    st.write("🌍 Real-Life Example")
    st.write("📝 Generate Quiz")
    st.write("📌 Summary")
    st.write("💡 Fun Facts")

st.title("🤖 AI Learning Buddy")

topic = st.text_input("Enter a Topic")

level = st.selectbox(
    "Difficulty",
    ["Beginner","Intermediate","Advanced"]
)

activity = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Summary",
        "Fun Facts"
    ]
)

if st.button("Generate"):

    if topic == "":
        st.warning("Enter a topic.")
    else:

        if activity=="Explain Concept":
            prompt=f"Explain {topic} in simple {level} level language with headings and examples."

        elif activity=="Real-Life Example":
            prompt=f"Give three real life examples of {topic}."

        elif activity=="Generate Quiz":
            prompt=f"Create five MCQs on {topic} with answers."

        elif activity=="Summary":
            prompt=f"Summarize {topic} in bullet points."

        else:
            prompt=f"Give five interesting facts about {topic}."

        with st.spinner("Generating..."):
            response=model.generate_content(prompt)

        st.success("Done!")

        st.write(response.text)

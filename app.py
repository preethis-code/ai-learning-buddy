import streamlit as st
import google.generativeai as genai
import os

# -------------------- API SETUP --------------------
api_key = os.environ["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3-flash-preview")

# -------------------- PAGE SETUP --------------------
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- THEME --------------------
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

with st.sidebar:
    st.title("🚀 AI Learning Buddy")

    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )
    st.session_state.dark_mode = dark_mode

# Theme colors
if dark_mode:
    bg = "#090D18"
    card = "#111827"
    text = "#F8FAFC"
    secondary = "#94A3B8"
    border = "#273449"
    accent = "#7C5CFC"
    input_bg = "#161D2C"
else:
    bg = "#F6F8FC"
    card = "#FFFFFF"
    text = "#172033"
    secondary = "#64748B"
    border = "#E2E8F0"
    accent = "#6547E8"
    input_bg = "#FFFFFF"

# -------------------- CUSTOM CSS --------------------
st.markdown(
    f"""
    <style>

    .stApp {{
        background:
            radial-gradient(circle at 80% 0%, {accent}18 0%, transparent 30%),
            {bg};
        color: {text};
    }}

    [data-testid="stSidebar"] {{
        background: {card};
        border-right: 1px solid {border};
    }}

    h1, h2, h3, p, label {{
        color: {text} !important;
    }}

    .hero {{
        padding: 35px 40px;
        border: 1px solid {border};
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            {card},
            {accent}18
        );
        margin-bottom: 28px;
    }}

    .hero h1 {{
        font-size: 48px;
        margin: 0;
    }}

    .hero p {{
        color: {secondary} !important;
        font-size: 18px;
        margin-top: 12px;
    }}

    .feature-card {{
        background: {card};
        border: 1px solid {border};
        border-radius: 16px;
        padding: 18px;
        min-height: 110px;
        transition: 0.3s;
    }}

    .feature-card:hover {{
        transform: translateY(-3px);
        border-color: {accent};
    }}

    .feature-card p {{
        color: {secondary} !important;
        font-size: 14px;
    }}

    div[data-testid="stTextInput"] input,
    div[data-testid="stTextArea"] textarea {{
        background: {input_bg};
        color: {text};
        border-radius: 12px;
    }}

    div[data-baseweb="select"] > div {{
        background: {input_bg};
        border-radius: 12px;
    }}

    .stButton > button {{
        background: linear-gradient(90deg, {accent}, #9B7BFF);
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        font-weight: 600;
        transition: 0.2s;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 25px {accent}55;
    }}

    .response-box {{
        background: {card};
        border: 1px solid {border};
        border-left: 4px solid {accent};
        border-radius: 16px;
        padding: 25px;
        margin-top: 20px;
    }}

    .footer {{
        text-align: center;
        color: {secondary};
        padding: 40px 0 15px 0;
        font-size: 14px;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# -------------------- PERSONA --------------------
PERSONA = """
You are Preethi, a friendly, patient, and encouraging AI Learning Buddy.
Teach learners in simple, beginner-friendly language using clear explanations
and relatable real-life examples. Break complex concepts into easy steps,
encourage curiosity, and provide constructive feedback.
"""

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.divider()

    st.markdown("### 🌌 Topic")
    st.write("**AI in Space Exploration**")

    st.markdown("### 🧭 Explore")
    st.write("📖 Explain Concepts")
    st.write("🌍 Real-Life Examples")
    st.write("📝 Generate Quizzes")
    st.write("💬 Ask Anything")
    st.write("✅ Evaluate Answers")

    st.divider()
    st.caption("Built with 🚀 by Preethi")

# -------------------- HERO --------------------
st.markdown(
    """
    <div class="hero">
        <h1>🚀 AI in Space Exploration</h1>
        <p>
        Discover how Artificial Intelligence helps spacecraft,
        astronauts and scientists explore the universe.
    </div>
    """,
    unsafe_allow_html=True
)

# -------------------- FEATURE CARDS --------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🪐 Learn</h3>
            <p>Understand complex space and AI concepts in simple language.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <h3>🧠 Practice</h3>
            <p>Generate quizzes and test your understanding instantly.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <h3>✨ Improve</h3>
            <p>Submit your answers and receive constructive AI feedback.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.markdown("## 🌠 Start Exploring")

# -------------------- INPUT --------------------
question = st.text_input(
    "What would you like to learn?",
    placeholder="Example: How does AI help Mars rovers navigate?"
)

activity = st.selectbox(
    "Choose a Learning Activity",
    [
        "📖 Explain Concept",
        "🌍 Real-Life Example",
        "📝 Generate Quiz",
        "💬 Ask Anything",
        "✅ Evaluate My Answer"
    ]
)

learner_answer = ""

if activity == "✅ Evaluate My Answer":
    learner_answer = st.text_area(
        "Your Answer",
        placeholder="Type your answer here..."
    )

# -------------------- GENERATE --------------------
if st.button("✨ Generate Response", use_container_width=True):

    if not question:
        st.warning("Please enter a question or topic.")

    else:

        if activity == "📖 Explain Concept":
            prompt = f"""
            {PERSONA}
            Explain {question} in simple, beginner-friendly language.
            Start with a clear definition, break it into easy points,
            give a simple analogy if helpful, and end with a short summary.
            """

        elif activity == "🌍 Real-Life Example":
            prompt = f"""
            {PERSONA}
            Give one clear real-life example related to {question}.
            Explain step by step how it works and why it is useful.
            """

        elif activity == "📝 Generate Quiz":
            prompt = f"""
            {PERSONA}
            Create a 5-question multiple-choice quiz about {question}.
            Give four options (A, B, C, D) for each question.
            Include the correct answer and a brief explanation.
            """

        elif activity == "💬 Ask Anything":
            prompt = f"""
            {PERSONA}
            Answer this learner's question clearly and accurately:
            {question}
            """

        else:
            if not learner_answer:
                st.warning("Please enter your answer.")
                st.stop()

            prompt = f"""
            {PERSONA}

            Question or topic: {question}
            Learner's answer: {learner_answer}

            Evaluate the answer for correctness and clarity.
            Explain what was done well, correct any mistakes,
            and give one simple suggestion for improvement.
            """

        with st.spinner("🚀 Exploring the universe..."):
            try:
                response = model.generate_content(prompt)

                st.success("Response generated successfully!")

                st.markdown(
                    """
                    <div class="response-box">
                    <h3>🤖 Your AI Learning Buddy Says</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# -------------------- FOOTER --------------------
st.markdown(
    """
    <div class="footer">
        🚀 AI Learning Buddy • AI in Space Exploration<br>
        Designed & Built by Preethi
    </div>
    """,
    unsafe_allow_html=True
)

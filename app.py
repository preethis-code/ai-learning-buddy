import streamlit as st
import google.generativeai as genai
import textwrap

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# API SETUP
# =========================================================
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-3-flash-preview")

# =========================================================
# SAFE HTML HELPER
# =========================================================
def render_html(content):
    st.markdown(
        textwrap.dedent(content).strip(),
        unsafe_allow_html=True
    )

# =========================================================
# THEME STATE
# =========================================================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

with st.sidebar:
    st.markdown("## 🚀 AI Learning Buddy")

    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

    st.session_state.dark_mode = dark_mode

# =========================================================
# THEME COLORS
# =========================================================
if dark_mode:
    BG = "#080C16"
    SIDEBAR = "#0D1424"
    SURFACE = "#111A2D"
    SURFACE_ALT = "#171D38"
    TEXT = "#F8FAFC"
    MUTED = "#A9B5CA"
    BORDER = "#293652"
    INPUT = "#111A2D"
    PLACEHOLDER = "#8390A5"
    ACCENT = "#7C5CFC"
    ACCENT_2 = "#A78BFA"
    HEADER = "#080C16"
else:
    BG = "#F5F7FC"
    SIDEBAR = "#FFFFFF"
    SURFACE = "#FFFFFF"
    SURFACE_ALT = "#F2EFFF"
    TEXT = "#172033"
    MUTED = "#5F6C80"
    BORDER = "#DCE3EE"
    INPUT = "#FFFFFF"
    PLACEHOLDER = "#7B8798"
    ACCENT = "#7657F6"
    ACCENT_2 = "#9B7CFF"
    HEADER = "#FFFFFF"

# =========================================================
# CSS
# =========================================================
st.markdown(
    f"""
<style>
[data-testid="stHeaderActionElements"] {
    display: none !important;
}
/* APP */
.stApp {{
    background:
        radial-gradient(circle at 90% 5%, {ACCENT}12, transparent 28%),
        {BG};
    color: {TEXT};
}}

/* HEADER */
[data-testid="stHeader"] {{
    background: {HEADER} !important;
    border-bottom: 1px solid {BORDER} !important;
}}

/* CONTENT - FIXES HEADER OVERLAP */
.block-container {{
    max-width: 1300px !important;
    padding-top: 6rem !important;
    padding-bottom: 4rem !important;
}}

/* SIDEBAR */
[data-testid="stSidebar"] {{
    background: {SIDEBAR} !important;
    border-right: 1px solid {BORDER} !important;
}}

[data-testid="stSidebar"] * {{
    color: {TEXT};
}}

/* GENERAL TEXT */
h1, h2, h3, h4, p, label {{
    color: {TEXT} !important;
}}

/* HERO */
.hero {{
    box-sizing: border-box;
    width: 100%;
    padding: 48px 52px;
    margin-bottom: 30px;
    border-radius: 26px;
    border: 1px solid {BORDER};
    background:
        radial-gradient(circle at 90% 10%, {ACCENT}30, transparent 30%),
        linear-gradient(135deg, {SURFACE}, {SURFACE_ALT});
    box-shadow: 0 18px 50px rgba(0,0,0,0.08);
}}

.hero-badge {{
    display: inline-block;
    padding: 8px 14px;
    margin-bottom: 26px;
    border-radius: 999px;
    border: 1px solid {ACCENT}55;
    background: {ACCENT}18;
    color: {ACCENT_2} !important;
    font-size: 13px;
    font-weight: 700;
}}

.hero-title {{
    margin: 0 !important;
    font-size: clamp(42px, 5vw, 66px) !important;
    line-height: 1.08 !important;
    letter-spacing: -2px;
    color: {TEXT} !important;
}}

.hero-description {{
    max-width: 900px;
    margin: 25px 0 0 0 !important;
    color: {MUTED} !important;
    font-size: 18px;
    line-height: 1.75;
}}

/* FEATURE CARDS */
.feature-card {{
    min-height: 185px;
    box-sizing: border-box;
    padding: 28px;
    border-radius: 20px;
    background: {SURFACE};
    border: 1px solid {BORDER};
    transition: 0.2s ease;
}}

.feature-card:hover {{
    transform: translateY(-4px);
    border-color: {ACCENT};
    box-shadow: 0 14px 35px {ACCENT}20;
}}

.feature-icon {{
    font-size: 29px;
    margin-bottom: 17px;
}}

.feature-title {{
    margin: 0 0 10px 0 !important;
    font-size: 23px;
}}

.feature-text {{
    margin: 0 !important;
    color: {MUTED} !important;
    line-height: 1.6;
}}

/* INPUT */
[data-testid="stTextInput"] input {{
    background: {INPUT} !important;
    color: {TEXT} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 12px !important;
    min-height: 52px !important;
}}

[data-testid="stTextInput"] input::placeholder {{
    color: {PLACEHOLDER} !important;
    opacity: 1 !important;
}}

/* TEXT AREA */
[data-testid="stTextArea"] textarea {{
    background: {INPUT} !important;
    color: {TEXT} !important;
    border: 1px solid {BORDER} !important;
    border-radius: 12px !important;
}}

[data-testid="stTextArea"] textarea::placeholder {{
    color: {PLACEHOLDER} !important;
    opacity: 1 !important;
}}

/* SELECT BOX */
[data-baseweb="select"] > div {{
    background: {INPUT} !important;
    color: {TEXT} !important;
    border-color: {BORDER} !important;
    border-radius: 12px !important;
    min-height: 52px !important;
}}

[data-baseweb="select"] * {{
    color: {TEXT} !important;
}}

/* DROPDOWN */
[role="listbox"] {{
    background: {SURFACE} !important;
    border: 1px solid {BORDER} !important;
}}

[role="option"] {{
    background: {SURFACE} !important;
    color: {TEXT} !important;
}}

[role="option"]:hover {{
    background: {SURFACE_ALT} !important;
}}

/* BUTTON */
.stButton > button {{
    width: 100%;
    min-height: 54px;
    margin-top: 8px;
    border: none !important;
    border-radius: 13px !important;
    color: white !important;
    font-size: 16px !important;
    font-weight: 700 !important;
    background: linear-gradient(
        100deg,
        {ACCENT},
        {ACCENT_2}
    ) !important;
    transition: 0.2s ease;
}}

.stButton > button:hover {{
    transform: translateY(-2px);
    box-shadow: 0 10px 30px {ACCENT}50;
}}

/* RESPONSE */
.response-title {{
    margin-top: 30px;
    padding: 20px 24px;
    border-radius: 16px;
    border: 1px solid {BORDER};
    border-left: 4px solid {ACCENT};
    background: {SURFACE};
}}

/* FOOTER */
.footer {{
    margin-top: 55px;
    padding: 28px 0;
    text-align: center;
    border-top: 1px solid {BORDER};
    color: {MUTED} !important;
    line-height: 1.8;
}}

/* MOBILE */
@media (max-width: 768px) {{
    .block-container {{
        padding-top: 5rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    .hero {{
        padding: 32px 25px;
    }}

    .hero-title {{
        font-size: 40px !important;
    }}
}}

</style>
""",
    unsafe_allow_html=True
)

# =========================================================
# AI PERSONA
# =========================================================
PERSONA = """
You are Preethi, a friendly, patient, and encouraging AI Learning Buddy.
You specialize in helping beginners understand AI in Space Exploration.
Use simple language, clear structure, relatable examples, and step-by-step
explanations. Encourage curiosity and provide constructive feedback.
"""

# =========================================================
# SIDEBAR
# =========================================================
with st.sidebar:
    st.divider()

    st.markdown("### 🌌 Current Topic")
    st.markdown("**AI in Space Exploration**")

    st.divider()

    st.markdown("### 🧭 Learning Tools")
    st.write("📖 Explain Concepts")
    st.write("🌍 Real-Life Examples")
    st.write("🧠 Generate Quizzes")
    st.write("💬 Ask Anything")
    st.write("✅ Evaluate Answers")

    st.divider()
    st.caption("Designed & Built by Preethi 🚀")

# =========================================================
# HERO
# =========================================================
render_html("""
<div class="hero">
    <div class="hero-badge">
        ✦ YOUR AI-POWERED SPACE LEARNING COMPANION
    </div>
    <h1 class="hero-title">
        Explore Space.<br>Learn with AI. 🚀
    </h1>
    <p class="hero-description">
        Discover how artificial intelligence helps rovers navigate Mars,
        scientists explore distant worlds, and spacecraft make intelligent
        decisions millions of kilometres from Earth.
    </p>
</div>
""")

# =========================================================
# FEATURE CARDS
# =========================================================
col1, col2, col3 = st.columns(3, gap="medium")

with col1:
    render_html("""
    <div class="feature-card">
        <div class="feature-icon">🪐</div>
        <h3 class="feature-title">Learn</h3>
        <p class="feature-text">
            Understand complex AI and space concepts through
            simple, beginner-friendly explanations.
        </p>
    </div>
    """)

with col2:
    render_html("""
    <div class="feature-card">
        <div class="feature-icon">🧠</div>
        <h3 class="feature-title">Practice</h3>
        <p class="feature-text">
            Generate quizzes instantly and test your understanding
            of AI in space exploration.
        </p>
    </div>
    """)

with col3:
    render_html("""
    <div class="feature-card">
        <div class="feature-icon">✨</div>
        <h3 class="feature-title">Improve</h3>
        <p class="feature-text">
            Submit your answers and receive clear,
            constructive feedback from your AI Learning Buddy.
        </p>
    </div>
    """)

st.write("")
st.write("")

# =========================================================
# LEARNING SECTION
# =========================================================
st.markdown("## 🌠 Start Exploring")

st.caption(
    "Choose a learning activity and ask anything about AI in space exploration."
)

question = st.text_input(
    "What would you like to learn?",
    placeholder="Example: How does AI help Mars rovers navigate?"
)

activity = st.selectbox(
    "Choose a Learning Activity",
    [
        "📖 Explain Concept",
        "🌍 Real-Life Example",
        "🧠 Generate Quiz",
        "💬 Ask Anything",
        "✅ Evaluate My Answer"
    ]
)

learner_answer = ""

if activity == "✅ Evaluate My Answer":
    learner_answer = st.text_area(
        "Enter your answer",
        placeholder="Type your answer here...",
        height=150
    )

# =========================================================
# GENERATE RESPONSE
# =========================================================
if st.button("✨ Generate Response"):

    if not question.strip():
        st.warning("🚀 Enter a question or topic to begin exploring.")

    else:

        if activity == "📖 Explain Concept":
            prompt = f"""
            {PERSONA}

            Explain this topic: {question}

            Use simple beginner-friendly language.
            Start with a clear definition.
            Break the explanation into easy points.
            Include a simple analogy if helpful.
            End with a short key takeaway.
            """

        elif activity == "🌍 Real-Life Example":
            prompt = f"""
            {PERSONA}

            Give one clear real-world example related to:
            {question}

            Explain step by step how it works,
            how AI is involved, and why it is useful.
            """

        elif activity == "🧠 Generate Quiz":
            prompt = f"""
            {PERSONA}

            Create a 5-question multiple-choice quiz about:
            {question}

            Give four options A, B, C and D.
            Include the correct answer and a short explanation
            for every question.
            """

        elif activity == "💬 Ask Anything":
            prompt = f"""
            {PERSONA}

            Answer this learner's question clearly and accurately:

            {question}
            """

        else:
            if not learner_answer.strip():
                st.warning(
                    "Please enter your answer before requesting feedback."
                )
                st.stop()

            prompt = f"""
            {PERSONA}

            Question or topic:
            {question}

            Learner's answer:
            {learner_answer}

            Evaluate the answer for correctness and clarity.
            Explain what was done well.
            Correct any mistakes.
            Give one simple suggestion for improvement.
            """

        with st.spinner(
            "🚀 Your AI Learning Buddy is exploring..."
        ):
            try:
                response = model.generate_content(prompt)

                render_html("""
                <div class="response-title">
                    <h3>🤖 Your Learning Buddy Says</h3>
                </div>
                """)

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# =========================================================
# FOOTER
# =========================================================
render_html("""
<div class="footer">
    🚀 <strong>AI Learning Buddy</strong> · AI in Space Exploration
    <br>
    Designed & Built by Preethi
</div>
""")

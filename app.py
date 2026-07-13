import streamlit as st
import google.generativeai as genai

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
# THEME STATE
# =========================================================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

# =========================================================
# SIDEBAR — THEME TOGGLE
# =========================================================
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
    BG = "#070B14"
    SIDEBAR = "#0D1424"
    SURFACE = "#111A2D"
    SURFACE_2 = "#172136"
    TEXT = "#F8FAFC"
    MUTED = "#A9B5CA"
    BORDER = "#293652"
    INPUT = "#111A2D"
    PLACEHOLDER = "#71809A"
    ACCENT = "#7C5CFC"
    ACCENT_2 = "#A78BFA"
    SHADOW = "rgba(0,0,0,0.25)"
else:
    BG = "#F5F7FC"
    SIDEBAR = "#FFFFFF"
    SURFACE = "#FFFFFF"
    SURFACE_2 = "#F1F4FA"
    TEXT = "#172033"
    MUTED = "#5F6C80"
    BORDER = "#DCE3EE"
    INPUT = "#FFFFFF"
    PLACEHOLDER = "#8A96A8"
    ACCENT = "#6547E8"
    ACCENT_2 = "#8B6CF6"
    SHADOW = "rgba(30,41,59,0.08)"

# =========================================================
# CUSTOM CSS
# =========================================================
st.markdown(
    f"""
    <style>

    /* MAIN APP */
    .stApp {{
        background:
            radial-gradient(circle at 85% 5%, {ACCENT}18 0%, transparent 28%),
            {BG};
        color: {TEXT};
    }}

    /* TOP HEADER / TOOLBAR */
    [data-testid="stHeader"] {{
        background: {BG} !important;
        border-bottom: 1px solid {BORDER};
    }}

    [data-testid="stToolbar"] {{
        color: {TEXT} !important;
    }}

    /* SIDEBAR */
    [data-testid="stSidebar"] {{
        background: {SIDEBAR} !important;
        border-right: 1px solid {BORDER};
    }}

    [data-testid="stSidebar"] * {{
        color: {TEXT};
    }}

    /* GENERAL TEXT */
    h1, h2, h3, h4, p, label {{
        color: {TEXT} !important;
    }}

    /* MAIN CONTENT WIDTH */
    .block-container {{
        max-width: 1250px;
        padding-top: 2.5rem;
        padding-bottom: 3rem;
    }}

    /* HERO */
    .hero {{
        position: relative;
        overflow: hidden;
        padding: 42px;
        margin-bottom: 28px;
        border-radius: 24px;
        border: 1px solid {BORDER};
        background:
            radial-gradient(circle at 90% 20%, {ACCENT}35 0%, transparent 25%),
            linear-gradient(135deg, {SURFACE}, {SURFACE_2});
        box-shadow: 0 15px 45px {SHADOW};
    }}

    .hero-badge {{
        display: inline-block;
        padding: 7px 13px;
        margin-bottom: 15px;
        border-radius: 999px;
        background: {ACCENT}22;
        color: {ACCENT_2} !important;
        font-size: 13px;
        font-weight: 700;
        border: 1px solid {ACCENT}55;
    }}

    .hero h1 {{
        font-size: clamp(36px, 5vw, 58px);
        line-height: 1.05;
        margin: 0;
        letter-spacing: -2px;
    }}

    .hero p {{
        max-width: 760px;
        color: {MUTED} !important;
        font-size: 18px;
        line-height: 1.7;
        margin: 16px 0 0 0;
    }}

    /* FEATURE CARDS */
    .feature-card {{
        height: 165px;
        padding: 24px;
        border-radius: 18px;
        border: 1px solid {BORDER};
        background: {SURFACE};
        box-shadow: 0 8px 25px {SHADOW};
        transition: all 0.25s ease;
    }}

    .feature-card:hover {{
        transform: translateY(-4px);
        border-color: {ACCENT};
        box-shadow: 0 15px 35px {ACCENT}18;
    }}

    .feature-icon {{
        font-size: 27px;
        margin-bottom: 10px;
    }}

    .feature-card h3 {{
        margin: 0 0 8px 0;
        font-size: 21px;
    }}

    .feature-card p {{
        color: {MUTED} !important;
        line-height: 1.55;
        font-size: 14px;
    }}

    /* TEXT INPUT */
    [data-testid="stTextInput"] input {{
        background: {INPUT} !important;
        color: {TEXT} !important;
        border: 1px solid {BORDER} !important;
        border-radius: 12px !important;
        min-height: 50px;
    }}

    [data-testid="stTextInput"] input::placeholder {{
        color: {PLACEHOLDER} !important;
        opacity: 1 !important;
    }}

    [data-testid="stTextInput"] input:focus {{
        border-color: {ACCENT} !important;
        box-shadow: 0 0 0 2px {ACCENT}25 !important;
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
        min-height: 50px;
    }}

    [data-baseweb="select"] span {{
        color: {TEXT} !important;
    }}

    /* DROPDOWN MENU */
    [data-baseweb="popover"] {{
        background: {SURFACE} !important;
    }}

    [role="listbox"] {{
        background: {SURFACE} !important;
        border: 1px solid {BORDER} !important;
    }}

    [role="option"] {{
        color: {TEXT} !important;
        background: {SURFACE} !important;
    }}

    [role="option"]:hover {{
        background: {SURFACE_2} !important;
    }}

    /* BUTTON */
    .stButton > button {{
        width: 100%;
        min-height: 52px;
        color: white !important;
        font-size: 16px;
        font-weight: 700;
        border: none !important;
        border-radius: 13px;
        background: linear-gradient(
            100deg,
            {ACCENT},
            {ACCENT_2}
        ) !important;
        transition: all 0.25s ease;
    }}

    .stButton > button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 30px {ACCENT}55;
    }}

    /* RESPONSE CARD */
    .response-header {{
        margin-top: 25px;
        padding: 20px 24px;
        background: linear-gradient(
            135deg,
            {SURFACE},
            {ACCENT}15
        );
        border: 1px solid {BORDER};
        border-left: 4px solid {ACCENT};
        border-radius: 16px;
    }}

    .response-header h3 {{
        margin: 0;
    }}

    /* DIVIDERS */
    hr {{
        border-color: {BORDER} !important;
    }}

    /* ALERTS */
    [data-testid="stAlert"] {{
        border-radius: 14px;
    }}

    /* FOOTER */
    .footer {{
        margin-top: 50px;
        padding-top: 25px;
        text-align: center;
        border-top: 1px solid {BORDER};
        color: {MUTED} !important;
        font-size: 14px;
        line-height: 1.8;
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
Teach using simple language, clear structure, relatable examples, and
step-by-step explanations. Encourage curiosity and provide constructive,
supportive feedback.
"""

# =========================================================
# SIDEBAR CONTENT
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

    st.caption("Designed & built by Preethi 🚀")

# =========================================================
# HERO
# =========================================================
st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">✦ YOUR AI-POWERED SPACE LEARNING COMPANION</div>
        <h1>Explore Space.<br>Learn with AI. 🚀</h1>
        <p>
            Discover how artificial intelligence helps rovers navigate Mars,
            scientists explore distant worlds, and spacecraft make intelligent
            decisions millions of kilometres from Earth.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FEATURE CARDS
# =========================================================
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🪐</div>
            <h3>Learn</h3>
            <p>Turn complex AI and space concepts into clear, beginner-friendly explanations.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">🧠</div>
            <h3>Practice</h3>
            <p>Generate quizzes instantly and strengthen your understanding of any topic.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        """
        <div class="feature-card">
            <div class="feature-icon">✨</div>
            <h3>Improve</h3>
            <p>Submit your own answers and receive supportive, constructive AI feedback.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

st.write("")
st.write("")

# =========================================================
# LEARNING AREA
# =========================================================
st.markdown("## 🌠 Start Your Learning Journey")
st.caption(
    "Choose a learning activity and ask anything about AI in space exploration."
)

question = st.text_input(
    "What would you like to learn?",
    placeholder="e.g. How does AI help Mars rovers navigate autonomously?"
)

activity = st.selectbox(
    "Choose a learning activity",
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
        "Your answer",
        placeholder="Type your answer here and receive constructive feedback...",
        height=150
    )

# =========================================================
# GENERATE RESPONSE
# =========================================================
if st.button("✨ Generate Learning Response"):

    if not question.strip():
        st.warning("🚀 Enter a question or topic to begin exploring.")

    else:

        if activity == "📖 Explain Concept":
            prompt = f"""
            {PERSONA}

            Explain this topic: {question}

            Use simple, beginner-friendly language.
            Start with a clear definition.
            Break the explanation into easy points.
            Include a simple analogy when useful.
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

            Give four options (A, B, C, D) for each question.
            Clearly provide the correct answer and a short explanation.
            """

        elif activity == "💬 Ask Anything":
            prompt = f"""
            {PERSONA}

            Answer the learner's question clearly and accurately:

            {question}
            """

        else:
            if not learner_answer.strip():
                st.warning("Please enter your answer before requesting feedback.")
                st.stop()

            prompt = f"""
            {PERSONA}

            Question or topic:
            {question}

            Learner's answer:
            {learner_answer}

            Evaluate the answer for correctness and clarity.
            Explain what the learner did well.
            Correct any mistakes clearly and kindly.
            Give one practical suggestion for improvement.
            """

        with st.spinner("🚀 Your AI Learning Buddy is exploring..."):
            try:
                response = model.generate_content(prompt)

                st.markdown(
                    """
                    <div class="response-header">
                        <h3>🤖 Your AI Learning Buddy Says</h3>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown(response.text)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

# =========================================================
# FOOTER
# =========================================================
st.markdown(
    """
    <div class="footer">
        🚀 <strong>AI Learning Buddy</strong> · AI in Space Exploration<br>
        Designed & Built by Preethi
    </div>
    """,
    unsafe_allow_html=True
)

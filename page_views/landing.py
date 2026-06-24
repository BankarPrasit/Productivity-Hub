import streamlit as st
import random
from components.theme import apply_global_ui


def landing_page():

    apply_global_ui()

    # ================= SESSION STATE INIT =================
    if "page" not in st.session_state:
        st.session_state.page = "landing"

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    # ================= CSS + HERO (COMBINED) =================
    st.markdown("""
    <style>

    .hero-container {
        text-align: center;
        padding-top: 70px;
        padding-bottom: 40px;
        animation: fadeUp 1s ease;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(40px); }
        to   { opacity: 1; transform: translateY(0px); }
    }

    .hero-badge {
        display: inline-block;
        padding: 10px 22px;
        border-radius: 40px;
        background: rgba(77,166,255,0.08);
        border: 1px solid rgba(77,166,255,0.2);
        color: #8ecbff !important;
        font-size: 14px;
        margin-bottom: 25px;
        backdrop-filter: blur(12px);
    }

    .hero-title {
        font-size: 84px !important;
        font-weight: 900 !important;
        color: #66b7ff !important;
        line-height: 1;
        margin-bottom: 20px;
        text-shadow:
            0 0 25px rgba(77,166,255,0.4),
            0 0 80px rgba(77,166,255,0.15);
    }

    .hero-sub {
        font-size: 22px !important;
        color: white !important;
        opacity: 0.85;
        line-height: 1.7;
        margin-bottom: 45px;
    }

    .feature-card {
        background: linear-gradient(135deg, rgba(18,28,50,0.55), rgba(10,18,35,0.82));
        border: 1px solid rgba(77,166,255,0.14);
        border-radius: 24px;
        padding: 30px;
        backdrop-filter: blur(18px);
        transition: 0.35s ease;
        height: 100%;
    }

    .feature-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 0 35px rgba(77,166,255,0.18);
    }

    .feature-title {
        color: #78c1ff !important;
        font-size: 26px !important;
        font-weight: 800 !important;
        margin-bottom: 18px;
    }

    .feature-text {
        line-height: 1.8;
        font-size: 15px !important;
        opacity: 0.9;
        color: white !important;
    }

    /* ── Step cards: flex row so all cards share the same height ── */
    .step-row {
        display: flex;
        gap: 16px;
        align-items: stretch;
    }

    .step-card {
        flex: 1;
        background: rgba(15,25,45,0.76);
        border: 1px solid rgba(77,166,255,0.14);
        border-radius: 24px;
        padding: 28px;
        text-align: center;
        transition: 0.35s ease;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        color: white !important;
        box-sizing: border-box;
    }

    .step-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 0 30px rgba(77,166,255,0.22);
    }

    .step-no {
        color: #66b7ff !important;
        font-size: 38px !important;
        font-weight: 900 !important;
        margin-bottom: 10px;
    }

    .step-title {
        color: #a0d4ff !important;
        font-size: 17px !important;
        font-weight: 700 !important;
        margin-bottom: 8px;
    }

    .step-desc {
        color: rgba(255,255,255,0.75) !important;
        font-size: 14px !important;
    }

    .motivation-card {
        background: linear-gradient(135deg, rgba(18,28,50,0.6), rgba(10,18,35,0.88));
        border: 1px solid rgba(77,166,255,0.15);
        border-radius: 28px;
        padding: 35px;
        text-align: center;
        backdrop-filter: blur(18px);
    }

    .motivation-title {
        color: #66b7ff !important;
        font-size: 28px !important;
        font-weight: 800 !important;
        margin-bottom: 16px;
    }

    .quote-text {
        font-size: 26px !important;
        font-weight: 700 !important;
        color: #9bd0ff !important;
    }

    .footer {
        text-align: center;
        opacity: 0.6;
        margin-top: 80px;
        padding-bottom: 30px;
        font-size: 14px;
        color: white !important;
    }

    </style>

    <div class="hero-container">
        <div class="hero-badge">
            AI Powered • Smart Workflow • Productivity System
        </div>
        <div class="hero-title">
            Productivity Hub
        </div>
        <div class="hero-sub">
            Next Generation AI Productivity Ecosystem<br>
            for Smart Task Management & Study Planning
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ================= BUTTONS =================
    col1, col2, col3 = st.columns(3)

    if col1.button("🚀 Get Started"):
        st.session_state.page = "login"
        st.rerun()

    if col2.button("📊 Dashboard"):
        if st.session_state.logged_in:
            st.session_state.page = "dashboard"
        else:
            st.session_state.page = "login"
        st.rerun()

    if col3.button("🤖 AI Assistant"):
        if st.session_state.logged_in:
            st.session_state.page = "ai"
        else:
            st.session_state.page = "login"
        st.rerun()

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ================= FEATURES =================
    st.subheader("✨ Platform Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📋 Smart Task System</div>
            <div class="feature-text">
                ✅ Task Management<br>
                ✅ Priority Levels<br>
                ✅ Due Date Tracking<br>
                ✅ Recurring Tasks<br>
                ✅ Kanban Workflow<br>
                ✅ Bulk Operations
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">📊 Productivity Analytics</div>
            <div class="feature-text">
                ✅ Smart Dashboard<br>
                ✅ Completion Analytics<br>
                ✅ Progress Insights<br>
                ✅ Productivity Score<br>
                ✅ Performance Tracking<br>
                ✅ Visual Reports
            </div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="feature-card">
            <div class="feature-title">🤖 AI Productivity Engine</div>
            <div class="feature-text">
                ✅ AI Task Generator<br>
                ✅ AI Study Planner<br>
                ✅ Smart Prioritization<br>
                ✅ Time Estimation<br>
                ✅ Daily Planner<br>
                ✅ Motivation System
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ================= WORKFLOW =================
    st.subheader("⚡ Workflow")

    steps = [
        ("01", "Create Tasks",   "Add goals, priorities and deadlines."),
        ("02", "AI Planning",    "AI generates smart workflows."),
        ("03", "Track Progress", "Analyze productivity using dashboard."),
        ("04", "Achieve Goals",  "Complete tasks efficiently with AI.")
    ]

    # All 4 cards in ONE markdown block inside a flex row —
    # this is the only reliable way to equalize heights in Streamlit.
    cards_html = "".join([
        f'<div class="step-card">'
        f'<div class="step-no">{s[0]}</div>'
        f'<div class="step-title">{s[1]}</div>'
        f'<div class="step-desc">{s[2]}</div>'
        f'</div>'
        for s in steps
    ])

    st.markdown(
        '<div class="step-row">' + cards_html + '</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ================= MOTIVATION =================
    quotes = [
        "Success starts with consistency.",
        "Discipline creates achievement.",
        "Small progress is still progress.",
        "Productivity beats procrastination.",
        "Your future depends on today."
    ]

    st.markdown(f"""
    <div class="motivation-card">
        <div class="motivation-title">⚡ Daily Motivation</div>
        <div class="quote-text">
            {random.choice(quotes)}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ================= FOOTER =================
    st.markdown("""
    <div class="footer">
        Productivity Hub • Premium AI Productivity Platform
    </div>
    """, unsafe_allow_html=True)
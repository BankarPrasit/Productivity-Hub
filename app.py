import streamlit as st

# ================= IMPORTS =================
from components.theme import apply_global_ui

from auth.login   import login_page
from auth.signup  import signup_page

from pages.landing               import landing_page
from pages.tasks.add_task        import add_task_page
from pages.tasks.manage_tasks    import manage_tasks_page
from pages.tasks.completed_tasks import completed_page
from pages.tasks.kanban_board    import kanban_board_page
from pages.dashboard             import dashboard
from pages.ai_assistant          import ai_page


# ================= PAGE CONFIG =================
st.set_page_config(
    page_title      = "Productivity Hub",
    page_icon="🚀",
    layout          = "wide",
    initial_sidebar_state = "collapsed"   # ← collapse sidebar on load
)

apply_global_ui()

# ================= SESSION STATES =================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "auth_page" not in st.session_state:
    st.session_state.auth_page = "login"

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "show_greeting" not in st.session_state:
    st.session_state.show_greeting = False

# ================= ROUTER =================

if not st.session_state.logged_in:

    if st.session_state.page == "landing":
        landing_page()

    elif st.session_state.auth_page == "signup":
        signup_page()

    else:
        login_page()

else:

    # ================= GREETING =================
    if st.session_state.show_greeting:

        user_name = ""
        if "user" in st.session_state and st.session_state.user:
            user_name = st.session_state.user.get("name", "")
            if not user_name:
                user_name = st.session_state.user.get(
                    "email", "User"
                ).split("@")[0]

        st.markdown(f"""
        <style>
        .greeting-overlay {{
            position:        fixed;
            top:             0;
            left:            0;
            width:           100vw;
            height:          100vh;
            background:      rgba(2,2,2,0.95);
            z-index:         9999;
            display:         flex;
            flex-direction:  column;
            align-items:     center;
            justify-content: center;
        }}
        .greet-emoji {{
            font-size:     72px;
            margin-bottom: 24px;
            animation:     bounceIn 0.6s ease;
        }}
        @keyframes bounceIn {{
            0%   {{ transform: scale(0.3); opacity: 0; }}
            60%  {{ transform: scale(1.1); }}
            100% {{ transform: scale(1);   opacity: 1; }}
        }}
        .greet-title {{
            font-size:   48px;
            font-weight: 900;
            color:       #66b7ff;
            text-shadow:
                0 0 30px rgba(77,166,255,0.6),
                0 0 80px rgba(77,166,255,0.2);
            margin-bottom: 12px;
        }}
        .greet-sub {{
            font-size:      20px;
            color:          rgba(255,255,255,0.65);
            letter-spacing: 1px;
        }}
        </style>

        <div class="greeting-overlay">
            <div class="greet-emoji">👋</div>
            <div class="greet-title">Welcome, {user_name.title()}!</div>
            <div class="greet-sub">Ready to boost your productivity?</div>
        </div>
        """, unsafe_allow_html=True)

        import time
        time.sleep(2.5)

        # ← after greeting go to dashboard
        st.session_state.show_greeting = False
        st.session_state.page          = "dashboard"
        st.rerun()

    # ================= PAGE ROUTER =================

    elif st.session_state.page == "dashboard":
        dashboard()

    elif st.session_state.page == "add_task":
        add_task_page()

    elif st.session_state.page == "manage_tasks":
        manage_tasks_page()

    elif st.session_state.page == "completed":
        completed_page()

    elif st.session_state.page == "kanban":
        kanban_board_page()

    elif st.session_state.page == "ai":
        ai_page()

    elif st.session_state.page == "landing":
        landing_page()

    else:
        st.session_state.page = "dashboard"
        st.rerun()
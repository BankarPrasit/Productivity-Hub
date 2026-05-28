import streamlit as st


def navbar():

    st.markdown("""
    <style>

    /* =========================================
       HIDE SIDEBAR + DRAWER COMPLETELY
    ========================================= */

    [data-testid="stSidebar"]                        { display: none !important; }
    [data-testid="collapsedControl"]                  { display: none !important; }
    section[data-testid="stSidebar"]                  { display: none !important; }
    [data-testid="stSidebarNav"]                      { display: none !important; }
    [data-testid="stSidebarNavItems"]                 { display: none !important; }
    button[kind="header"]                             { display: none !important; }
    .st-emotion-cache-zq5wmm                          { display: none !important; }
    .st-emotion-cache-1cypcdb                         { display: none !important; }
    .st-emotion-cache-eczf16                          { display: none !important; }
    #MainMenu                                         { display: none !important; }
    header                                            { display: none !important; }
    footer                                            { display: none !important; }

    /* =========================================
       NAVBAR WRAPPER
    ========================================= */

    .navbar-wrap {
        background:      rgba(8,16,35,0.9);
        padding:         12px 20px;
        border-radius:   16px;
        border:          1px solid rgba(77,166,255,0.18);
        margin-bottom:   28px;
        backdrop-filter: blur(16px);
        box-shadow:      0 0 30px rgba(77,166,255,0.08);
    }

    /* =========================================
       NAV BUTTONS
    ========================================= */

    [data-testid="stHorizontalBlock"] .stButton > button {
        width:          100%                              !important;
        padding:        7px 4px                           !important;
        font-size:      12px                              !important;
        font-weight:    600                               !important;
        border-radius:  10px                              !important;
        white-space:    nowrap                            !important;
        min-height:     38px                              !important;
        line-height:    1.2                               !important;
        background:     transparent                       !important;
        border:         1px solid rgba(77,166,255,0.18)   !important;
        color:          rgba(255,255,255,0.75)             !important;
        box-shadow:     none                              !important;
        letter-spacing: 0.3px                             !important;
        transition:     all 0.25s ease                    !important;
    }

    [data-testid="stHorizontalBlock"] .stButton > button:hover {
        background:   rgba(77,166,255,0.12)               !important;
        border-color: rgba(77,166,255,0.5)                !important;
        color:        #66b7ff                             !important;
        transform:    translateY(-2px)                    !important;
        box-shadow:   0 0 14px rgba(77,166,255,0.2)       !important;
    }

    [data-testid="stHorizontalBlock"] .stButton > button:active {
        transform:  scale(0.96)                           !important;
        background: rgba(77,166,255,0.2)                  !important;
    }

    /* =========================================
       LOGOUT BUTTON — GLASS BLUE
    ========================================= */

    [data-testid="stHorizontalBlock"] .stButton:last-child > button {
        background:   rgba(77,166,255,0.08)               !important;
        border-color: rgba(77,166,255,0.35)               !important;
        color:        #66b7ff                             !important;
        box-shadow:   0 0 12px rgba(77,166,255,0.12)      !important;
    }

    [data-testid="stHorizontalBlock"] .stButton:last-child > button:hover {
        background:   rgba(77,166,255,0.18)               !important;
        border-color: rgba(77,166,255,0.6)                !important;
        color:        #a8d8ff                             !important;
        box-shadow:   0 0 20px rgba(77,166,255,0.3)       !important;
        transform:    translateY(-2px)                    !important;
    }

    </style>
    <div class="navbar-wrap"></div>
    """, unsafe_allow_html=True)

    # ================= USER BADGE =================
    user_name = ""
    if "user" in st.session_state and st.session_state.user:
        user_name = st.session_state.user.get("name", "")
        if not user_name:
            user_name = st.session_state.user.get(
                "email", ""
            ).split("@")[0]

    # ================= NAV ITEMS =================
    col_nav, col_user = st.columns([7, 1])

    with col_nav:

        c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)

        nav_items = [
            (c1, "🏠 Home",      "landing"),
            (c2, "➕ Add",       "add_task"),
            (c3, "📋 Manage",    "manage_tasks"),
            (c4, "✅ Done",      "completed"),
            (c5, "📊 Dashboard", "dashboard"),
            (c6, "🤖 AI",        "ai"),
            (c7, "📌 Kanban",    "kanban"),
            (c8, "🚪 Logout",    "logout"),
        ]

        for col, label, page in nav_items:
            with col:
                if st.button(label, key=f"nav_{page}"):
                    if page == "logout":
                        st.session_state.logged_in     = False
                        st.session_state.page          = "landing"
                        st.session_state.user          = None
                        st.session_state.show_greeting = False
                    else:
                        st.session_state.page = page
                    st.rerun()

    with col_user:
        if user_name:
            st.markdown(f"""
            <div style="
                text-align:    center;
                font-size:     12px;
                font-weight:   700;
                color:         #66b7ff;
                background:    rgba(77,166,255,0.08);
                border:        1px solid rgba(77,166,255,0.2);
                border-radius: 10px;
                padding:       7px 6px;
                white-space:   nowrap;
                overflow:      hidden;
                text-overflow: ellipsis;
            ">
                👤 {user_name.title()}
            </div>
            """, unsafe_allow_html=True)
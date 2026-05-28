import streamlit as st
from auth.auth_utils import login_user


def login_page():

    # ================= CSS =================
    st.markdown("""
    <style>

    .title-style {
        text-align:  center;
        font-size:   58px;
        font-weight: 900;
        color:       #5ab0ff !important;
        margin-bottom: 10px;
    }

    .subtitle-style {
        text-align: center;
        opacity:    0.8;
        font-size:  18px;
        margin-bottom: 40px;
        color:      white !important;
    }

    .hero-card {
        background: linear-gradient(
            135deg,
            rgba(13,94,255,0.15),
            rgba(58,160,255,0.08)
        );
        border:        1px solid rgba(77,166,255,0.25);
        border-radius: 16px;
        padding:       22px 28px;
        margin-bottom: 20px;
        text-align:    center;
        backdrop-filter: blur(12px);
    }

    .hero-card-title {
        font-size:     20px !important;
        font-weight:   800 !important;
        color:         #66b7ff !important;
        margin-bottom: 8px;
    }

    .hero-card-text {
        font-size:  13px !important;
        color:      rgba(255,255,255,0.6) !important;
        line-height: 1.7 !important;
    }

    .hero-card-badges {
        display:    flex;
        justify-content: center;
        gap:        10px;
        margin-top: 14px;
        flex-wrap:  wrap;
    }

    .badge {
        background:    rgba(77,166,255,0.1);
        border:        1px solid rgba(77,166,255,0.2);
        border-radius: 20px;
        padding:       4px 12px;
        font-size:     12px !important;
        color:         #8ecbff !important;
    }

    .divider-text {
        text-align:  center;
        font-size:   12px;
        color:       rgba(255,255,255,0.3);
        margin:      10px 0;
        position:    relative;
    }

    .divider-text::before,
    .divider-text::after {
        content:    "";
        position:   absolute;
        top:        50%;
        width:      38%;
        height:     1px;
        background: rgba(77,166,255,0.15);
    }

    .divider-text::before { left:  0; }
    .divider-text::after  { right: 0; }

    .forgot-link {
        text-align:  right;
        font-size:   12px;
        color:       rgba(77,166,255,0.7) !important;
        cursor:      pointer;
        margin-top:  4px;
        margin-bottom: 8px;
    }

    .forgot-link:hover {
        color: #66b7ff !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # ================= TITLE =================
    st.markdown(
        '<h1 class="title-style">Productivity Hub</h1>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<p class="subtitle-style">AI-powered productivity management platform</p>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # ================= LOGIN CARD =================
    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        # ---- HERO CARD (fills the empty space) ----
        st.markdown("""
        <div class="hero-card">
            <div class="hero-card-title">
                ⚡ Welcome to Productivity Hub
            </div>
            <div class="hero-card-text">
                Your AI-powered workspace for smart task management,<br>
                study planning and productivity analytics.
            </div>
            <div class="hero-card-badges">
                <span class="badge">🤖 AI Powered</span>
                <span class="badge">📋 Task Manager</span>
                <span class="badge">📊 Analytics</span>
                <span class="badge">📌 Kanban</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # ---- LOGIN FORM ----
        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.subheader("🚀 Login Account")

        email    = st.text_input("📧 Email")
        password = st.text_input("🔒 Password", type="password")

        # ---- FORGOT PASSWORD TOGGLE ----
        if "show_forgot" not in st.session_state:
            st.session_state.show_forgot = False

        col_a, col_b = st.columns([2, 1])

        with col_b:
            if st.button(
                "🔑 Forgot Password?",
                key="forgot_btn"
            ):
                st.session_state.show_forgot = not st.session_state.show_forgot

        # ---- FORGOT PASSWORD SECTION ----
        if st.session_state.show_forgot:

            st.markdown("""
            <div style="
                background:    rgba(77,166,255,0.06);
                border:        1px solid rgba(77,166,255,0.2);
                border-radius: 12px;
                padding:       16px 18px;
                margin-bottom: 12px;
            ">
                <div style="font-size:13px; color:#78c1ff; font-weight:700; margin-bottom:10px;">
                    🔑 Reset Password
                </div>
                <div style="font-size:12px; color:rgba(255,255,255,0.55); margin-bottom:10px;">
                    Enter your registered email to reset your password.
                </div>
            </div>
            """, unsafe_allow_html=True)

            reset_email = st.text_input(
                "📧 Enter your registered email",
                key="reset_email"
            )

            if st.button("📩 Send Reset Link", key="reset_btn"):

                if reset_email:

                    # Load users and check email
                    from auth.auth_utils import load_users
                    users = load_users()
                    found = any(
                        u["email"] == reset_email for u in users
                    )

                    if found:
                        st.success(
                            f"✅ Password reset link sent to **{reset_email}**"
                        )
                        st.info(
                            "💡 For now, please contact admin or check your registered email."
                        )
                    else:
                        st.error(
                            "❌ No account found with this email address."
                        )
                else:
                    st.warning("⚠️ Please enter your email address.")

            st.markdown(
                '<div class="divider-text">or login below</div>',
                unsafe_allow_html=True
            )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("🚀 Login"):

            user = login_user(email, password)

            if user:
                st.session_state.logged_in     = True
                st.session_state.user          = user
                st.session_state.page          = "dashboard"
                st.session_state.show_greeting = True
                st.session_state.show_forgot   = False
                st.rerun()

            else:
                st.error("❌ Invalid email or password.")

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            '<div class="divider-text">don\'t have an account?</div>',
            unsafe_allow_html=True
        )

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button("✨ Create New Account"):
            st.session_state.auth_page   = "signup"
            st.session_state.show_forgot = False
            st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)

    # ================= FOOTER =================
    st.markdown("""
    <div style="
        text-align:  center;
        margin-top:  50px;
        opacity:     0.6;
        font-size:   14px;
        color:       white;
    ">
        Productivity Hub • Smart Workflow • AI Productivity
    </div>
    """, unsafe_allow_html=True)
import streamlit as st

from auth.auth_utils import signup_user


def signup_page():

    st.markdown("""
    <div class="glass fade-in">
        <h1 style="text-align:center;">
        Create Account
        </h1>
    </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Sign Up"):

        created = signup_user(
            name,
            email,
            password
        )

        if created:

            st.success("Account Created 🚀")

            st.session_state.auth_page = "login"

            st.rerun()

        else:

            st.error("Email already exists")

    st.markdown("---")

    if st.button("Back to Login"):

        st.session_state.auth_page = "login"

        st.rerun()
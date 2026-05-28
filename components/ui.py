import streamlit as st

# ---------- TITLE ----------
def title(text):
    st.markdown(f"<h1 style='color:#4da6ff;text-align:center'>{text}</h1>", unsafe_allow_html=True)


# ---------- CARD ----------
def card(title, subtitle):
    st.markdown(f"""
    <div style="
        background: rgba(10,20,40,0.6);
        border: 1px solid rgba(77,166,255,0.2);
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 10px;
    ">
        <h3 style="color:#4da6ff;">{title}</h3>
        <p>{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)


# ---------- BACK BUTTON ----------
def back_button():
    if st.button("🔙 Back to Home"):
        st.session_state.page = "landing"
        st.rerun()


# ---------- METRICS BOX ----------
def metric_box(label, value):
    st.markdown(f"""
    <div style="
        background: rgba(10,20,40,0.6);
        padding: 15px;
        border-radius: 10px;
        border: 1px solid rgba(77,166,255,0.2);
        text-align:center;
    ">
        <h4 style="color:#4da6ff">{label}</h4>
        <h2>{value}</h2>
    </div>
    """, unsafe_allow_html=True)
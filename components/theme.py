import streamlit as st

def apply_global_ui():

    st.markdown("""
    <style>

    /* =========================================
       HIDE SIDEBAR — UPDATED FOR STREAMLIT 1.40+
    ========================================= */
    [data-testid="stSidebar"]                        { display: none !important; }
    [data-testid="collapsedControl"]                  { display: none !important; }
    section[data-testid="stSidebar"]                  { display: none !important; }
    [data-testid="stSidebarNav"]                      { display: none !important; }
    [data-testid="stBaseButton-headerNoPadding"]      { display: none !important; }
    [data-testid="stHeaderActionElements"]            { display: none !important; }
    button[data-testid="baseButton-header"]           { display: none !important; }
    .st-emotion-cache-zq5wmm                          { display: none !important; }
    .st-emotion-cache-1cypcdb                         { display: none !important; }
    .st-emotion-cache-eczf16                          { display: none !important; }
    #MainMenu                                         { display: none !important; }
    header                                            { display: none !important; }
    footer                                            { display: none !important; }

    /* =========================================
       PURE BLACK PREMIUM BACKGROUND
    ========================================= */

    .stApp {
        background: #020202 !important;
        color: white !important;
        overflow-x: hidden;
    }

    /* =========================================
       ANIMATED GRID LINES
    ========================================= */

    .stApp::before {
        content: "";
        position: fixed;
        width: 100%;
        height: 100%;
        top: 0;
        left: 0;
        z-index: -2;
        background-image:
            linear-gradient(rgba(77,166,255,0.06) 1px, transparent 1px),
            linear-gradient(90deg, rgba(77,166,255,0.06) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: gridMove 14s linear infinite;
    }

    @keyframes gridMove {
        from { background-position: 0 0; }
        to   { background-position: 50px 50px; }
    }

    /* =========================================
       FLOATING BLUE GLOW
    ========================================= */

    .stApp::after {
        content: "";
        position: fixed;
        width: 600px;
        height: 600px;
        background: radial-gradient(circle, rgba(77,166,255,0.18), transparent 70%);
        top: -200px;
        right: -120px;
        z-index: -1;
        animation: floatingGlow 8s ease-in-out infinite;
    }

    @keyframes floatingGlow {
        0%   { transform: translateY(0px); }
        50%  { transform: translateY(30px); }
        100% { transform: translateY(0px); }
    }

    /* =========================================
       FADE ANIMATION
    ========================================= */

    .fade-in {
        animation: fadeInUp 1s ease;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(40px); }
        to   { opacity: 1; transform: translateY(0px); }
    }

    /* =========================================
       BLOCK CONTAINER — FULL WIDTH FIX
    ========================================= */

    .block-container {
        padding-top:    1.5rem !important;
        padding-bottom: 2rem   !important;
        padding-left:   2rem   !important;
        padding-right:  2rem   !important;
        max-width:      100%   !important;
        margin: 0 auto !important;
    }

    /* =========================================
       GLASS CARDS
    ========================================= */

    .glass {
        background: linear-gradient(135deg, rgba(15,25,45,0.55), rgba(5,10,20,0.82));
        border: 1px solid rgba(77,166,255,0.15);
        backdrop-filter: blur(16px);
        border-radius: 18px;
        padding: 20px 24px;
        margin-bottom: 16px;
        overflow: hidden;
        position: relative;
        transition: all 0.35s ease;
        box-shadow: 0 0 25px rgba(77,166,255,0.08), inset 0 0 12px rgba(255,255,255,0.03);
    }

    .glass::before {
        content: "";
        position: absolute;
        width: 180%;
        height: 180%;
        top: -120%;
        left: -30%;
        background: linear-gradient(to bottom right, rgba(255,255,255,0.08), rgba(255,255,255,0));
        transform: rotate(25deg);
        transition: 0.8s;
    }

    .glass:hover::before { top: 120%; }

    .glass:hover {
        transform: translateY(-4px);
        border: 1px solid rgba(77,166,255,0.35);
        box-shadow: 0 0 30px rgba(77,166,255,0.18), 0 0 60px rgba(77,166,255,0.06);
    }

    /* =========================================
       GLASS TEXT SIZES
    ========================================= */

    .glass h3 {
        font-size: 18px !important;
        color: #78c1ff !important;
        margin-bottom: 10px !important;
    }

    .glass h4 {
        font-size: 15px !important;
        color: #a0d4ff !important;
        margin-bottom: 6px !important;
    }

    .glass p, .glass b {
        font-size: 14px !important;
        color: rgba(255,255,255,0.85) !important;
        line-height: 1.7 !important;
    }

    /* =========================================
       BUTTONS — MAIN
    ========================================= */

    .stButton > button {
        width: 100% !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        border: none !important;
        font-weight: 700 !important;
        font-size: 15px !important;
        color: white !important;
        background: linear-gradient(135deg, #0d5eff, #3aa0ff) !important;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(77,166,255,0.25);
    }

    .stButton > button:hover {
        transform: translateY(-2px) !important;
        background: linear-gradient(135deg, #1970ff, #66c2ff) !important;
        box-shadow: 0 0 25px rgba(77,166,255,0.4) !important;
    }

    .stButton > button:active {
        transform: scale(0.97) !important;
        background: linear-gradient(135deg, #0949c9, #1d8fff) !important;
    }

    /* =========================================
       INPUTS
    ========================================= */

    .stTextInput input,
    .stTextArea textarea,
    .stDateInput input {
        background: rgba(10,20,40,0.75) !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(77,166,255,0.18) !important;
        font-size: 14px !important;
        padding: 10px 14px !important;
    }

    .stTextInput input::placeholder,
    .stTextArea textarea::placeholder {
        color: rgba(255,255,255,0.3) !important;
    }

    .stTextInput input:focus,
    .stTextArea textarea:focus {
        border: 1px solid rgba(77,166,255,0.5) !important;
        box-shadow: 0 0 12px rgba(77,166,255,0.18) !important;
        outline: none !important;
    }

    /* =========================================
       SELECTBOX
    ========================================= */

    [data-testid="stSelectbox"] > div > div {
        background: rgba(10,20,40,0.75) !important;
        color: white !important;
        border-radius: 12px !important;
        border: 1px solid rgba(77,166,255,0.18) !important;
        font-size: 14px !important;
    }

    /* =========================================
       METRICS
    ========================================= */

    [data-testid="metric-container"] {
        background: rgba(10,20,40,0.7);
        border-radius: 16px;
        padding: 16px 20px;
        border: 1px solid rgba(77,166,255,0.15);
        box-shadow: 0 0 18px rgba(77,166,255,0.07);
        transition: 0.3s;
    }

    [data-testid="metric-container"]:hover {
        transform: translateY(-3px);
        box-shadow: 0 0 25px rgba(77,166,255,0.18);
    }

    [data-testid="metric-container"] label {
        font-size: 13px !important;
        color: rgba(255,255,255,0.6) !important;
    }

    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        font-size: 28px !important;
        color: #5ab0ff !important;
        font-weight: 800 !important;
    }

    /* =========================================
       HEADINGS
    ========================================= */

    [data-testid="stMarkdownContainer"] > h1,
    [data-testid="stMarkdownContainer"] > h2,
    [data-testid="stMarkdownContainer"] > h3,
    div[data-testid="stHeadingWithActionElements"] h1,
    div[data-testid="stHeadingWithActionElements"] h2,
    div[data-testid="stHeadingWithActionElements"] h3 {
        color: #5ab0ff !important;
        text-shadow: 0 0 18px rgba(77,166,255,0.2);
        font-size: 22px !important;
    }

    div[data-testid="stHeadingWithActionElements"] h1 {
        font-size: 28px !important;
    }

    /* =========================================
       PROGRESS BAR
    ========================================= */

    .stProgress > div > div {
        background: linear-gradient(90deg, #0d5eff, #3aa0ff) !important;
        border-radius: 10px !important;
    }

    /* =========================================
       RADIO & CHECKBOX
    ========================================= */

    .stRadio label,
    .stCheckbox label {
        color: white !important;
        font-size: 14px !important;
    }

    /* =========================================
       DATAFRAME
    ========================================= */

    [data-testid="stDataFrame"] {
        border-radius: 14px !important;
        overflow: hidden;
        border: 1px solid rgba(77,166,255,0.15) !important;
    }

    /* =========================================
       SCROLLBAR
    ========================================= */

    ::-webkit-scrollbar       { width: 8px; }
    ::-webkit-scrollbar-track { background: #020202; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(#1d6dff, #4da6ff);
        border-radius: 20px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(#3a80ff, #66b7ff);
    }

    /* =========================================
       SPINNER
    ========================================= */

    .stSpinner > div {
        border-top-color: #4da6ff !important;
    }

    /* =========================================
       PAGE TITLE
    ========================================= */

    .page-title {
        font-size: 26px !important;
        font-weight: 800 !important;
        color: #5ab0ff !important;
        margin-bottom: 20px !important;
        text-shadow: 0 0 18px rgba(77,166,255,0.2);
    }

    /* =========================================
       DIVIDER
    ========================================= */

    hr {
        border-color: rgba(77,166,255,0.1) !important;
        margin: 16px 0 !important;
    }

    </style>
    """, unsafe_allow_html=True)

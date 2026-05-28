import streamlit as st
from components.navbar import navbar
from utils.db import load_tasks


def completed_page():

    navbar()

    st.markdown('<div class="page-title">✅ Completed Tasks</div>', unsafe_allow_html=True)

    tasks           = load_tasks()
    completed_tasks = [t for t in tasks if t.get("done", False)]

    if not completed_tasks:
        st.markdown("""
        <div class="glass" style="text-align:center; padding:40px;">
            <div style="font-size:36px; margin-bottom:12px;">🎯</div>
            <div style="color:rgba(255,255,255,0.5); font-size:15px;">
                No completed tasks yet. Keep going!
            </div>
        </div>
        """, unsafe_allow_html=True)
        return

    st.markdown(f"""
    <div class="glass" style="text-align:center; padding:16px;">
        <div style="font-size:22px; font-weight:800; color:#5ab0ff;">
            🎉 {len(completed_tasks)} Task{"s" if len(completed_tasks) > 1 else ""} Completed
        </div>
    </div>
    """, unsafe_allow_html=True)

    for t in completed_tasks:

        priority_color = {
            "High":   "#ff6b6b",
            "Medium": "#ffd93d",
            "Low":    "#6bff9e"
        }.get(t.get("priority", "Medium"), "white")

        st.markdown(f"""
        <div class="glass">
            <div style="font-size:16px; font-weight:700; color:#a0d4ff; margin-bottom:10px;">
                ✅ {t.get('title', 'Untitled Task')}
            </div>
            <div style="font-size:13px; color:rgba(255,255,255,0.7); line-height:1.8;">
                <span style="color:{priority_color};">🔥 {t.get('priority', 'Medium')}</span>
                &nbsp;|&nbsp; 📅 {t.get('due', 'Not Set')}
                &nbsp;|&nbsp; 📌 {t.get('status', 'Completed')}
            </div>
        </div>
        """, unsafe_allow_html=True)
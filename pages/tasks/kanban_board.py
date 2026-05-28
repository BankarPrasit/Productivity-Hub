import streamlit as st
from components.navbar import navbar
from utils.db import load_tasks, save_tasks


def kanban_board_page():

    navbar()

    st.markdown('<div class="page-title">📌 Kanban Board</div>', unsafe_allow_html=True)

    tasks = load_tasks()

    todo_col, progress_col, done_col = st.columns(3)

    col_config = [
        (todo_col,     "Todo",        "🔵 Todo",        "#3aa0ff"),
        (progress_col, "In Progress", "🟡 In Progress",  "#ffd93d"),
        (done_col,     "Completed",   "🟢 Completed",    "#6bff9e"),
    ]

    for col, status_key, label, color in col_config:
        with col:
            st.markdown(f"""
            <div style="
                font-size: 16px;
                font-weight: 800;
                color: {color};
                margin-bottom: 14px;
                padding: 10px 16px;
                background: rgba(10,20,40,0.6);
                border-radius: 12px;
                border: 1px solid rgba(77,166,255,0.15);
                text-align: center;
            ">
                {label}
            </div>
            """, unsafe_allow_html=True)

            col_tasks = [t for t in tasks if t["status"] == status_key]

            if not col_tasks:
                st.markdown("""
                <div style="
                    text-align:center;
                    padding: 20px;
                    color: rgba(255,255,255,0.3);
                    font-size: 13px;
                ">No tasks</div>
                """, unsafe_allow_html=True)

            for t in col_tasks:

                priority_color = {
                    "High":   "#ff6b6b",
                    "Medium": "#ffd93d",
                    "Low":    "#6bff9e"
                }.get(t["priority"], "white")

                st.markdown(f"""
                <div class="glass" style="margin-bottom:10px;">
                    <div style="font-size:14px; font-weight:700; color:#a0d4ff; margin-bottom:8px;">
                        {t['title']}
                    </div>
                    <div style="font-size:12px; color:rgba(255,255,255,0.65); line-height:1.7;">
                        <span style="color:{priority_color};">🔥 {t['priority']}</span><br>
                        📅 {t['due']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if status_key == "Todo":
                    if st.button("➡ In Progress", key=f"todo_{t['id']}"):
                        t["status"] = "In Progress"
                        save_tasks(tasks)
                        st.rerun()

                elif status_key == "In Progress":
                    if st.button("✅ Complete", key=f"prog_{t['id']}"):
                        t["status"] = "Completed"
                        t["done"]   = True
                        save_tasks(tasks)
                        st.rerun()
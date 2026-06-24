import streamlit as st
from components.navbar import navbar
from utils.db import load_tasks, save_tasks


def manage_tasks_page():

    navbar()

    st.markdown('<div class="page-title">📋 Manage Tasks</div>', unsafe_allow_html=True)

    tasks = load_tasks()

    # ---- FILTERS ----
    f1, f2 = st.columns(2)

    with f1:
        search = st.text_input("🔍 Search Tasks")

    with f2:
        priority_filter = st.selectbox("🔥 Filter Priority", ["All", "High", "Medium", "Low"])

    # ---- BULK ACTIONS ----
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:15px; font-weight:700; color:#78c1ff; margin-bottom:12px;">⚡ Bulk Actions</div>', unsafe_allow_html=True)

    b1, b2 = st.columns(2)

    with b1:
        if st.button("✅ Mark All Completed"):
            for t in tasks:
                t["done"]   = True
                t["status"] = "Completed"
            save_tasks(tasks)
            st.rerun()

    with b2:
        if st.button("🗑 Delete Completed"):
            tasks = [t for t in tasks if not t["done"]]
            save_tasks(tasks)
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---- FILTER LOGIC ----
    filtered = [
        t for t in tasks
        if search.lower() in t["title"].lower()
        and (priority_filter == "All" or t["priority"] == priority_filter)
    ]

    if not filtered:
        st.markdown("""
        <div class="glass" style="text-align:center; padding:30px;">
            <div style="color:rgba(255,255,255,0.5); font-size:15px;">No tasks found.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # ---- TASK LIST ----
    for t in filtered:

        status_icon = "✅" if t["done"] else "⏳"

        priority_color = {
            "High":   "#ff6b6b",
            "Medium": "#ffd93d",
            "Low":    "#6bff9e"
        }.get(t["priority"], "white")

        st.markdown(f"""
        <div class="glass">
            <div style="font-size:16px; font-weight:700; color:#a0d4ff; margin-bottom:10px;">
                {status_icon} {t['title']}
            </div>
            <div style="font-size:13px; color:rgba(255,255,255,0.7); line-height:1.8;">
                <span style="color:{priority_color};">🔥 {t['priority']}</span> &nbsp;|&nbsp;
                📅 {t['due']} &nbsp;|&nbsp;
                📌 {t['status']} &nbsp;|&nbsp;
                🏷 {", ".join(t['tags'])}
            </div>
        </div>
        """, unsafe_allow_html=True)

        c1, c2 = st.columns(2)

        with c1:
            if st.button("✔ Toggle Done", key=f"toggle_{t['id']}"):
                t["done"]   = not t["done"]
                t["status"] = "Completed" if t["done"] else "Todo"
                save_tasks(tasks)
                st.rerun()

        with c2:
            if st.button("🗑 Delete", key=f"delete_{t['id']}"):
                tasks.remove(t)
                save_tasks(tasks)
                st.rerun()
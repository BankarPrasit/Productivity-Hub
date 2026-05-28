import streamlit as st
from components.navbar import navbar
from utils.db import load_tasks, save_tasks


def add_task_page():

    navbar()

    st.markdown('<div class="page-title">➕ Add Task</div>', unsafe_allow_html=True)

    tasks = load_tasks()

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        with st.form("task_form", clear_on_submit=True):

            title       = st.text_input("📝 Task Title")
            description = st.text_area("📄 Description", height=90)

            r1, r2 = st.columns(2)

            with r1:
                priority = st.selectbox("🔥 Priority", ["Low", "Medium", "High"])

            with r2:
                status = st.selectbox("📌 Status", ["Todo", "In Progress", "Completed"])

            tags      = st.text_input("🏷 Tags (comma separated)")
            due       = st.date_input("📅 Due Date")
            recurring = st.checkbox("🔁 Recurring Task")
            subtasks  = st.text_area("📋 Subtasks (comma separated)", height=70)

            st.markdown("<br>", unsafe_allow_html=True)

            submit = st.form_submit_button("🚀 Add Task")

            if submit and title:

                new_task = {
                    "id":          len(tasks) + 1,
                    "title":       title,
                    "description": description,
                    "priority":    priority,
                    "tags":        [t.strip() for t in tags.split(",") if t.strip()],
                    "due":         str(due),
                    "done":        status == "Completed",
                    "recurring":   recurring,
                    "subtasks":    [s.strip() for s in subtasks.split(",") if s.strip()],
                    "status":      status
                }

                tasks.append(new_task)
                save_tasks(tasks)

                st.success("Task Added Successfully 🚀")

            elif submit and not title:
                st.error("Please enter a task title.")

        st.markdown("</div>", unsafe_allow_html=True)
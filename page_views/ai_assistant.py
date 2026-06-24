import streamlit as st
import random

from components.navbar import navbar
from utils.db import load_tasks, save_tasks


def ai_page():

    navbar()

    st.markdown('<div class="page-title">🤖 AI Productivity Assistant</div>', unsafe_allow_html=True)

    tasks = load_tasks()

    # ---- MOTIVATION ----
    quotes = [
        "Discipline creates success.",
        "Small progress is still progress.",
        "Focus on consistency.",
        "Your future depends on today.",
        "Productivity beats procrastination."
    ]

    st.markdown(f"""
    <div class="glass" style="text-align:center; padding:20px;">
        <div style="font-size:13px; color:rgba(255,255,255,0.5); margin-bottom:8px;">⚡ Daily Motivation</div>
        <div style="font-size:18px; font-weight:700; color:#9bd0ff;">
            {random.choice(quotes)}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---- AI TASK GENERATOR ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">🚀 AI Task Generator</div>', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])

    with col1:
        goal = st.text_input("Enter Your Goal", placeholder="e.g. prepare for exam, fitness, project...")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        generate = st.button("⚡ Generate")

    if generate and goal:

        task_map = {
            "exam":    ["Revise important topics", "Solve previous papers", "Practice MCQs", "Prepare notes", "Revision session"],
            "project": ["Research project topic", "Create project structure", "Design UI", "Develop backend", "Testing & debugging"],
            "fitness": ["Morning workout", "Drink enough water", "Track calories", "Evening walk", "Sleep on time"],
        }

        generated = next(
            (v for k, v in task_map.items() if k in goal.lower()),
            ["Break goal into steps", "Create schedule", "Focus on priority tasks", "Track progress", "Complete review"]
        )

        for g in generated:

            c1, c2, c3 = st.columns([3, 1, 1])

            with c1:
                st.markdown(f"""
                <div class="glass" style="padding:14px 18px; margin-bottom:0;">
                    <div style="font-size:14px; font-weight:600; color:#a0d4ff;">✅ {g}</div>
                    <div style="font-size:12px; color:rgba(255,255,255,0.5);">AI Generated Task</div>
                </div>
                """, unsafe_allow_html=True)

            with c2:
                if st.button("➕ Add", key=f"add_{g}"):
                    priority = "High" if any(w in g.lower() for w in ["exam", "revision", "testing"]) else \
                               "Low"  if any(w in g.lower() for w in ["practice", "research"]) else "Medium"
                    tasks.append({
                        "id": len(tasks) + 1, "title": g,
                        "description": "AI Generated Task", "priority": priority,
                        "tags": ["AI"], "due": "Not Set", "done": False,
                        "recurring": False, "subtasks": [], "status": "Todo"
                    })
                    save_tasks(tasks)
                    st.success(f"Added: {g} 🚀")
                    st.rerun()

            with c3:
                if st.button("⚡ Done", key=f"quick_{g}"):
                    tasks.append({
                        "id": len(tasks) + 1, "title": g,
                        "description": "AI Completed", "priority": "Medium",
                        "tags": ["AI"], "due": "Not Set", "done": True,
                        "recurring": False, "subtasks": [], "status": "Completed"
                    })
                    save_tasks(tasks)
                    st.success(f"Completed: {g} ✅")
                    st.rerun()

    st.markdown("---")

    # ---- AI STUDY PLANNER ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">📚 AI Study Planner</div>', unsafe_allow_html=True)

    s1, s2 = st.columns([3, 1])

    with s1:
        subject = st.text_input("Enter Subject", placeholder="e.g. DBMS, Java, Python, DSA, OS...")

    with s2:
        st.markdown("<br>", unsafe_allow_html=True)
        plan_btn = st.button("📚 Generate Plan")

    if plan_btn and subject:

        plan_map = {
            "dbms":   ["Introduction to DBMS", "ER Diagram & Keys", "Normalization", "SQL Queries Practice", "Transactions & PYQs"],
            "java":   ["OOP Concepts", "Inheritance & Polymorphism", "Exception Handling", "Collections Framework", "Java Programs Practice"],
            "python": ["Python Basics", "Functions & OOP", "File Handling", "Libraries & APIs", "Projects Practice"],
            "dsa":    ["Arrays & Strings", "Linked List", "Stack & Queue", "Trees & Graphs", "Sorting & Practice"],
            "os":     ["Process Management", "CPU Scheduling", "Deadlocks", "Memory Management", "Numericals & Revision"],
        }

        plan = next(
            (v for k, v in plan_map.items() if k in subject.lower()),
            ["Introduction", "Core Concepts", "Practice Problems", "Revision", "Final Test"]
        )

        st.markdown(f"""
        <div class="glass" style="text-align:center; padding:14px; margin-bottom:16px;">
            <div style="font-size:16px; font-weight:700; color:#78c1ff;">
                📚 Study Plan: {subject}
            </div>
        </div>
        """, unsafe_allow_html=True)

        p_cols = st.columns(5)

        for i, (col, topic) in enumerate(zip(p_cols, plan), start=1):
            with col:
                st.markdown(f"""
                <div class="glass" style="text-align:center; padding:14px;">
                    <div style="font-size:20px; font-weight:900; color:#66b7ff;">Day {i}</div>
                    <div style="font-size:13px; color:rgba(255,255,255,0.8); margin-top:8px;">✅ {topic}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")

    # ---- PRODUCTIVITY ANALYZER ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">📊 AI Productivity Analyzer</div>', unsafe_allow_html=True)

    total      = len(tasks)
    completed  = len([t for t in tasks if t["done"]])
    pending    = total - completed
    score      = round((completed / total) * 100) if total > 0 else 0

    a1, a2, a3, a4 = st.columns(4)

    a1.metric("📋 Total",       total)
    a2.metric("✅ Completed",    completed)
    a3.metric("⏳ Pending",      pending)
    a4.metric("⚡ Score",        f"{score}%")

    st.markdown("---")

    # ---- SMART PRIORITIZATION ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">🔥 AI Smart Prioritization</div>', unsafe_allow_html=True)

    high = [t for t in tasks if t["priority"] == "High" and not t["done"]]

    if high:
        for t in high:
            st.warning(f"🔥 High Priority: **{t['title']}**")
    else:
        st.success("✅ No urgent high-priority tasks pending.")

    st.markdown("---")

    # ---- DAILY PLANNER ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">🗓 AI Daily Planner</div>', unsafe_allow_html=True)

    pending_tasks = [t for t in tasks if not t["done"]][:5]

    if pending_tasks:
        for i, t in enumerate(pending_tasks, start=1):
            st.markdown(f"""
            <div class="glass" style="padding:14px 18px;">
                <div style="font-size:14px; font-weight:700; color:#a0d4ff;">
                    {i}. {t['title']}
                </div>
                <div style="font-size:12px; color:rgba(255,255,255,0.6); margin-top:4px;">
                    🔥 {t['priority']} &nbsp;|&nbsp; 📌 {t['status']}
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.success("🎉 All tasks completed!")

    st.markdown("---")

    # ---- TIME ESTIMATION ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">⏱ AI Time Estimation</div>', unsafe_allow_html=True)

    if pending_tasks:
        estimated = len(pending_tasks) * 2
        st.info(f"⏱ Estimated time to complete pending tasks: **{estimated} hours**")

    st.markdown("---")

    # ---- REMINDER SYSTEM ----
    st.markdown('<div style="font-size:18px; font-weight:700; color:#5ab0ff; margin-bottom:12px;">🔔 AI Reminders</div>', unsafe_allow_html=True)

    reminders = [t for t in tasks if not t["done"]][:3]

    if reminders:
        for t in reminders:
            st.error(f"🔔 Reminder: Complete **'{t['title']}'** soon.")
    else:
        st.success("🎉 All tasks completed!")
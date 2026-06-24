import streamlit as st
import pandas as pd
import plotly.express as px

from components.navbar import navbar
from utils.db import load_tasks

def dashboard():

    navbar()

    st.title("📊 Dashboard")

    tasks = load_tasks()

    total = len(tasks)

    done = len([
        t for t in tasks if t["done"]
    ])

    pending = total - done

    c1, c2, c3 = st.columns(3)

    c1.metric("Total", total)
    c2.metric("Completed", done)
    c3.metric("Pending", pending)

    if total > 0:

        st.progress(done / total)

        st.write(
            f"Efficiency: {round((done/total)*100,2)}%"
        )

        df = pd.DataFrame(tasks)

        fig = px.bar(
            df,
            x="priority",
            color="done"
        )

        st.plotly_chart(fig)
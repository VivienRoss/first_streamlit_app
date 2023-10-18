import streamlit as st
from streamlit_metrics import metric, metric_row
import pandas as pd
import numpy as np

st.write("## Here's a single figure")
metric("Metric 0", 0)

st.write("## ... and here's a row of them")
metric_row(
    {
        "Total des ventes": 45.236 ,
        "# Tickets": 200,
        "Metric 3": 300,
        "Metric 4": 400,
        "Metric 5": 500,
    }
)


import streamlit as st


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Ventes 2023", "Ventes 2022", "Target"])

st.line_chart(chart_data)

import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

col1, col2, col3 = st.columns(3)
col1.metric("Total des Ventes", "52.636 €", "5,2 %")
col2.metric("# Tickets ", "522", "-8%")
col3.metric("test", "86%", "4%")



chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Ventes 2023", "Ventes 2022", "Target"])

st.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)

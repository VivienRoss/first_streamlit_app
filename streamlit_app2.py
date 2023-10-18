import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total des Ventes", "52.636 €", "5,2 %")
col2.metric("# Tickets ", "522", "-8%")
col3.metric("test", "86%", "4%")
col4.metric("abc", "8.655", "-2%")


chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Ventes 2023", "Ventes 2022"])

st.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)

chart_data = pd.DataFrame(np.random.randn(5, 1), columns=["Produit"])

st.bar_chart(chart_data)

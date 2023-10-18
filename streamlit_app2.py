import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

tab1, tab2 = st.tabs(["📈 Vue d'ensemble", "🗃 Details"])

tab1.subheader("Information des ventes du jour pour le magasin XX") 

col1, col2, col3, col4 = tab1.columns(4)
col1.metric("Total des Ventes", "52.636 €", "5,2 %")
col2.metric("# Tickets ", "522", "-8%")
col3.metric("test", "86%", "4%")
col4.metric("abc", "8.655", "-2%")

tab1.markdown("""---""")

chart_data = pd.DataFrame(
   {"Produits": list(range(10)), "CY": np.random.randn(20), "LY": np.random.randn(20)}
)

tab1.bar_chart(
   chart_data, x="Produits", y=["CY", "LY"], color=["#FF0000", "#0000FF"]  
)

tab2.subheader("Details des ventes")

chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Ventes 2023", "Ventes 2022"])

tab2.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

tab2.table(df)



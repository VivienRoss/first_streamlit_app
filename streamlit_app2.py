import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

tab1, tab2 = st.tabs(["📈 Vue d'ensemble", "🗃 Details"])

tab1.subheader("Information des ventes du jour pour le magasin XX") 

col1, col2, col3, col4 = st.columns(4)
col1.tab1.metric("Total des Ventes", "52.636 €", "5,2 %")
tab1.metric("# Tickets ", "522", "-8%")
tab1.metric("test", "86%", "4%")
tab1.metric("abc", "8.655", "-2%")

chart_data = pd.DataFrame(np.random.randn(5, 1), columns=["Produit"])

tab1.bar_chart(chart_data)

tab2.subheader("Details des ventes")

chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Ventes 2023", "Ventes 2022"])

tab2.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

tab2.table(df)



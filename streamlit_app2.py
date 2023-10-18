import streamlit as st
import pandas as pd
import numpy as np

import streamlit as st

tab1, tab2 = st.tabs(["📈 Overviewe", "🗃 Details"])

tab1.subheader("Sales Overview") 

col1, col2, col3, col4 = tab1.columns(4)
col1.metric("Total Sales", "52.636 €", "5,2 %")
col2.metric("# Tickets ", "522", "-8%")
col3.metric("Margin", "32%", "4%")
col4.metric("Target", "60.000 €", "-12.2%")

tab1.markdown("""---""")

chart_data = pd.DataFrame(
   {"Produits": ["Product1","Product2","Product3","Product4","Product5"], "CY": np.random.randn(5), "LY": np.random.randn(5)}
)

tab1.bar_chart(
   chart_data, x="Produits", y=["CY", "LY"], color=["#FF0000", "#0000FF"]  
)

tab2.subheader("Sales Details")

chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Ventes 2023", "Ventes 2022"])

tab2.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

tab2.table(df)



import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
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
   {"Produits": ["Product 1","Product 2","Product 3","Product 4","Product 5"], "CY": np.random.randn(5), "LY": np.random.randn(5)}
)


tab1.Chart(chart_data).mark_bar().encode(
    x="Produits",
    y=["CY", "LY"]
)

tab2.subheader("Sales Details")

chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["Ventes 2023", "Ventes 2022"])

tab2.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

tab2.table(df)



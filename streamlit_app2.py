import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
import pydeck as pdk

tab1, tab2, tab3 = st.tabs(["📈 Overview", "🗃 Details", "Other visuals"])

tab1.subheader("Sales Overview") 

tab1.text('Le Lorem Ipsum est simplement du faux texte employé dans la composition')
tab1.text('et la mise en page avant impression.')
tab1.markdown("""---""")

col1, col2, col3, col4 = tab1.columns(4)
col1.metric("Total Sales", "52.636 €", "5,2 %")
col2.metric("# Tickets ", "522", "-8%")
col3.metric("Margin", "32%", "4%")
col4.metric("Target", "60.000 €", "-12.2%")

chart_data = pd.DataFrame({"Products":["Product 1","Product 2","Product 3","Product 4","Product 5"], "CY": np.random.randn(5),"LY": np.random.randn(5)})

tab1.bar_chart(
   chart_data, x="Products", y=["CY", "LY"], color=["#FF0000", "#0000FF"]  
) 



tab2.subheader("Sales Details")

chart_data = pd.DataFrame(np.random.randn(12, 2), columns=["Sales 2023", "Sales 2022"])

tab2.line_chart(chart_data)

df = pd.DataFrame(np.random.randn(12, 5), columns=(["Product 1","Product 2","Product 3","Product 4","Product 5"]))

tab2.table(df)

tab3.subheader("Other visuals")

chart_data = pd.DataFrame({"Products":["Product 1","Product 2","Product 3","Product 4","Product 5"], "Sales": np.random.randn(5),"Margin": np.random.randn(5)})

tab3.scatter_chart(
    chart_data,
    x='Sales',
    y='Margin',
   color='Products',
)

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
   columns=['lat', 'lon'])

tab3.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=37.76,
        longitude=-122.4,
        zoom=11,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))

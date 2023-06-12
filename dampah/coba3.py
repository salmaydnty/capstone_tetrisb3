import pandas as pd
import pydeck as pdk
import streamlit as st

SCATTERPLOT_LAYER_DATA = "air_sanitasi_2022.csv"
scatt = pd.read_csv(SCATTERPLOT_LAYER_DATA)
scatt["latitude"] = pd.to_numeric(scatt["latitude"], errors="coerce")
scatt["longitude"] = pd.to_numeric(scatt["longitude"], errors="coerce")

# Menambahkan kolom "negara" dan mengonversi nilainya menjadi tipe string
scatt["Negara"] = scatt["Negara"].astype(str)

# Create a ScatterplotLayer
scatterplot_layer = pdk.Layer(
    "ScatterplotLayer",
    data=scatt,
    opacity=0.8,
    stroked=True,
    filled=False,
    radius_scale=6,
    radius_min_pixels=1,
    radius_max_pixels=1000,
    line_width_min_pixels=5,
    get_position=["longitude", "latitude"],
    get_radius="radius",
    get_fill_color=[255, 140, 0],
    get_line_color=[0, 0, 0],
    get_text=["Negara", "Safely managed-National"],
    get_color=[0, 0, 0],
    pickable=True,
    auto_highlight=True,
)

# Create a Deck and render in Streamlit
deck = pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=scatt["latitude"].mean(),
        longitude=scatt["longitude"].mean(),
        zoom=5,
        pitch=0,
    ),
    layers=[scatterplot_layer],
)

# Render the deck using st.pydeck_chart()
st.title("ScatterplotLayer Example")
st.pydeck_chart(deck)

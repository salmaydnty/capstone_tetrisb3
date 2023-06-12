import pandas as pd
import pydeck as pdk
import streamlit as st

SCATTERPLOT_LAYER_DATA = "air_sanitasi_2022.csv"
df = pd.read_csv(SCATTERPLOT_LAYER_DATA)
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Create a ScatterplotLayer
scatterplot_layer = pdk.Layer(
    "ScatterplotLayer",
    data=df,
    opacity=0.8,
    stroked=True,
    filled=False,
    radius_scale=6,
    radius_min_pixels=1,
    radius_max_pixels=1000,
    line_width_min_pixels=5,
    get_position=["longitude", "latitude"],
    get_radius="radius",
    get_fill_color="fill_color",
    get_line_color="line_color",
    # Menambahkan kolom negara dan Safely managed-National sebagai teks pada hover
    get_text=["Negara", "Safely managed-National"],
    get_color=[0, 0, 0],  # Warna teks pada hover
    pickable=True,
    auto_highlight=True,
)

# Create a Deck and render in Streamlit
deck = pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=df["latitude"].mean(),
        longitude=df["longitude"].mean(),
        zoom=5,
        pitch=0,
    ),
    layers=[scatterplot_layer],
)

# Render the deck using st.pydeck_chart()
st.title("ScatterplotLayer Example")
st.pydeck_chart(deck)

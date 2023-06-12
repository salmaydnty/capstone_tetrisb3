import pandas as pd
import pydeck as pdk
import streamlit as st

SCATTERPLOT_LAYER_DATA = "air_sanitasi_2022.csv"
df = pd.read_csv(SCATTERPLOT_LAYER_DATA)
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Create a Streamlit app
st.title("ScatterplotLayer Example")
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=df["latitude"].mean(),
        longitude=df["longitude"].mean(),
        zoom=5,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            data=df,
            pickable=True,
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
        ),
    ],
))

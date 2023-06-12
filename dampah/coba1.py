import pandas as pd
import pydeck as pdk
import streamlit as st

# SCATTERPLOT_LAYER_DATA = "air_sanitasi_2022.csv"
# df = pd.read_csv(SCATTERPLOT_LAYER_DATA)

# # df = pd.read_csv("air_sanitasi_2022.csv")
# # df = df.dropna()
# # df = df[["Wastewater treated-National", "longitude", "latitude"]]
# df["latitude"] = pd.to_numeric(df["latitude"], downcast="float")
# df["longitude"] = pd.to_numeric(df["longitude"], downcast="float")
# # df.columns = ["Wastewater treated-National", "longitude", "latitude"]
# # st.map(df)


# Create a Streamlit app

df = pd.read_csv("air_sanitasi_2022.csv")
df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

# Create a Streamlit app
st.title("ScatterplotLayer Example")
st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=df["latitude"].values,
        longitude=df["longitude"].values,
        zoom=5,
        pitch=0,
    ),
    layers=[
        pdk.Layer(
            "ScatterplotLayer",
            df,
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=False,
            radius_scale=6,
            radius_min_pixels=1,
            radius_max_pixels=1000,
            line_width_min_pixels=5,
            get_position="[longitude, latitude]",
            get_radius="radius",
            get_fill_color=[255, 140, 0],
            get_line_color=[255, 140, 0],
        ),
    ],
))

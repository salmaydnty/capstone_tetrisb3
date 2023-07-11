import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
import altair as alt
import pydeck as pdk
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


# dasboard
st.header("Apakah Penyebaran Persediaan Air dan Sanitasi di Indonesia Sudah Baik?")
"by Salma Eka Yudanti (salmaey2022@gmail.com)"
st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify;font-size:20px;">UNICEF &#40;United Nations Children&#39;s Fund&#41; adalah organisasi PBB\
    yang bertujuan untuk meningkatan kualitas hidup anak maupun wanita yang berada di negara-negara berkembang.\
     </div>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div style="text-align:justify;font-size:20px;">Program Pemantauan Bersama WHO/UNICEF untuk Pasokan Air, Sanitasi, dan Kebersihan (JMP) membuat\
 perkiraan kemajuan dalam air minum, sanitasi, dan kebersihan (WASH) yang dapat dibandingkan di seluruh negara.\
 Ini juga bertanggung jawab untuk melacak target Tujuan Pembangunan Berkelanjutan (SDG) terkait WASH di seluruh dunia.\
     </div>', unsafe_allow_html=True)
image = Image.open('UNICEF_Logo.png')
st.image(image, caption='UNICEF scr: google.com')
st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div style="text-align:justify;font-size:20px;">Sejak tahun 2000, indikator pembangunan air dan sanitasi serta target MDGs telah diperbaiki. Dengan demikian, pertanyaan pemantauan telah berubah.\
    Program Pemantauan Bersama WHO-UNICEF (JMP) berisi kriteria yang tepat untuk menilai kemajuan menuju target air dan sanitasi.\
            </div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">Laporan penilaian global pertama WHO dan UNICEF</div>',
            unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">30%</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;font-weight:bold;">tidak memiliki</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;"> akses ke air minum yang bersih</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">60%</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;font-weight:bold;">membutuhkan sanitasi</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">yang bersih</div>',
                unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)
    st.markdown('<br>', unsafe_allow_html=True)

st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;">Tahun 2020</div>',
            unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)

col3, col4, col5 = st.columns([1, 1, 1])
with col3:
    st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">74%</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;font-weight:bold;"> menggunakan </div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">layanan air bersih</div>',
                unsafe_allow_html=True)
with col4:
    st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">138</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;font-weight:bold;">negara</div>',
                unsafe_allow_html=True)
with col5:
    st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;"> 45% </div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:25px;font-weight:bold;">dari</div>',
                unsafe_allow_html=True)
    st.markdown('<div style="text-align: center;font-size:20px;font-weight:bold;">populasi dunia</div>',
                unsafe_allow_html=True)


st.markdown('<div style="text-align: center;font-size:40px;font-weight:bold;"> >99% </div>',
            unsafe_allow_html=True)
st.markdown('<div style="text-align: center;font-size:30px;font-weight:bold;">coveraged</div>',
            unsafe_allow_html=True)
st.markdown("---")

# indonesia not included in
st.markdown('<div style="text-align:justify;font-size:20px;">Peta di bawah adalah sebaran data negara-negara dengan kemajuan menuju target air \
     yang lebih baik pada Tahun 2020. Indonesia tidak termasuk diantaranya kenapa ini bisa terjadi? </div >', unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)

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
    get_line_color=[116, 194, 225],
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
st.pydeck_chart(deck)


st.markdown('<br>', unsafe_allow_html=True)

# heatmap
st.markdown('<div  style="text-align:justify; font-size:30px;" > Korelasi Heatmap</div >',
            unsafe_allow_html=True)


@st.cache_data  # 👈 Add the caching decorator
def load_data(url):
    df = pd.read_csv(url)
    return df


df = load_data(
    "https://raw.githubusercontent.com/salmaydnty/capstone_tetrisb3/main/air_sanitasi_2022.csv")
z = df[['Disposed in situ-National', 'Emptied and treated-National', 'Wastewater treated-National',
        'Latrines and other-National', 'Septic tanks-National', 'Sewer connections-National']].corr()
fig = px.imshow(z, text_auto=True)
st.plotly_chart(fig, theme="streamlit")

st.markdown('<div  style="text-align:justify; font-size:20px;" > Apakah saja faktor yang mempengaruhi air bersih?</div >',
            unsafe_allow_html=True)
st.markdown('<div  style="text-align:justify; font-size:20px;" > Dari hasil korelasi ini menunjukkan bahwa ada 2 faktor\
    yaitu Air Limbah (Wastewater Treated) dan Saluran Pembuangan (Sewer connections). </div >',
            unsafe_allow_html=True)

st.markdown('<br>', unsafe_allow_html=True)
# st.markdown('<div div style="text-align:justify;font-size:20px;" > Terdapat korelasi yang kuat antara banyaknya\
#     air limbah dengan nilai variabel dikelola dengan aman (r=0,829). Hal ini menunjukkan bahwa air limbah dapat\
#         mempengaruhi terhadap pengelolaan air bersih. </div>', unsafe_allow_html=True)
# st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div  style="text-align:justify; font-size:20px;" > Menurut data Bank Dunia, hanya 2 % dari 10 juta penduduk pusat kota Jakarta\
    yang memiliki akses ke saluran air limbah umum. Sebagian besar perumahan perkotaan memiliki tangki septik\
        (septic tank), tetapi bocor dan merembes ke dalam tanah, sehingga jarang membutuhkan penyedot debu. Kotoran rumah tangga\
            yang disedot biasanya tidak dikirim ke instalasi pengolahan air limbah. Menurut data Bank Dunia, 95 % air limbah Indonesia\
                tumpah ke ladang pertanian, sungai, dan saluran terbuka. Ini memiliki efek kesehatan yang sangat besar.</div >', unsafe_allow_html=True)
st.markdown("---")

# from train import load_data
df = pd.read_csv('air_sanitasi_2022.csv')

# linear regression
# st.markdown('<div  style="text-align:center; font-size:40px;" >Analisis Korelasi</div >',
#             unsafe_allow_html=True)
# st.markdown('<div  style="text-align:center; font-size:30px;" >Korelasi antara Pengelolaan Air dengan Air Limbah.</div >', unsafe_allow_html=True)

# df['Safely managed-National'] = (df['Safely managed-National'] - df['Safely managed-National'].min()) / (
#     df['Safely managed-National'].max() - df['Safely managed-National'].min())
# df['Wastewater treated-National'] = (df['Wastewater treated-National'] - df['Wastewater treated-National'].min()) / (
#     df['Wastewater treated-National'].max() - df['Wastewater treated-National'].min())

# scatt = px.scatter(df, x=df['Safely managed-National'], y=df['Wastewater treated-National'], color="Negara",
#                    trendline="ols", trendline_scope="overall")
# scatt.update_traces(marker_size=10, showlegend=True)

# # finding linear regression model
# results = px.get_trendline_results(scatt)
# alpha = results.iloc[0]["px_fit_results"].params[0]
# beta = results.iloc[0]["px_fit_results"].params[1]
# rsq = results.iloc[0]["px_fit_results"].rsquared

# scatt.data[2].name = 'y = ' + str(round(alpha, 2)) + ' + ' + str(
#     round(beta, 8)) + 'x' + ' | R-squared = ' + str(round(rsq, 3))
# scatt.data[2].showlegend = True
# st.plotly_chart(scatt, use_container_width=True)


# st.markdown("---")


# top 5 and down 5
df2 = pd.read_csv('IPAL_2021.csv')
# st.dataframe(df2)

top5, down5 = st.columns(2)
with top5:
    st.write(
        '**Top 10 Daftar Provinsi dengan Jumlah Pelanggan Instalasi Pengolahan Air Limbah**')

    c = alt.Chart(df2.head(10)).mark_bar(interpolate='basis').encode(
        x='Jumlah_Pelanggan', y=alt.Y('Provinsi', sort='-x'),  color='Provinsi:N', tooltip=['Jumlah_Pelanggan', 'Provinsi'])

    st.altair_chart(c)
with down5:
    st.write(
        '**Down 10 Daftar Provinsi dengan Jumlah Pelanggan Instalasi Pengolahan Air Limbah**')

    c = alt.Chart(df2.tail(10)).mark_bar(interpolate='basis').encode(
        x='Jumlah_Pelanggan', y=alt.Y('Provinsi', sort='x'),  color='Provinsi:N', tooltip=['Jumlah_Pelanggan', 'Provinsi'])

    st.altair_chart(c)

st.markdown('<div div style="text-align:justify;font-size:20px;" > Menurut data yang diambil dari website Open Data PUPR (Kementerian Pekerjaan Umum dan Perumahan Rakyat)\
    Indonesia belum melakukan penyebaran pada pengolahan air limbah pada 2021. Ini menjadi evaluasi untuk pemerintah melakukan penyebaran pengolahan air limbah\
        terutama pada Pulau Sumatra, Kalimantan, dan Sulawesi.</div>', unsafe_allow_html=True)

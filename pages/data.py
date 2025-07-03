import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#---------------------------------
# Dados
#---------------------------------

#path_json = "plantio_refinado.json"
#df = pd.read_json(path_json)

path_csv = "sensor_data.csv"
df = pd.read_csv(path_csv)

#---------------------------------
# Tratamento
#---------------------------------

#df = df.T

df['Latitude'] = round(df['Latitude'], 2)
df['Longitude'] = round(df['Longitude'], 2)
df['coordenada'] = tuple((row['Latitude'], row['Longitude']) for _, row in df.iterrows())
df['coordenada_str'] = df['Latitude'].astype(str) + ';' + df['Longitude'].astype(str)

# Como tratar um string em datetime no pandas?
df["data_datetime"] = pd.to_datetime(arg=df['Data e Hora'], yearfirst=True) 

#---------------------------------
# Sidebar
#---------------------------------

st.sidebar.title("Filtros")

with st.sidebar:
    coordenadas = df['coordenada_str'].unique()
    f_coordenada = st.selectbox("Coordenata", coordenadas)

query = '''coordenada_str in @f_coordenada'''

df = df.query(query)

#---------------------------------
# Gráficos
#---------------------------------

fig_umidade = px.line(df,
                      x='data_datetime',
                      y='Umidade',
                      title="Umidade por Data")
fig_umidade.update_layout(xaxis_title="Data", yaxis_title="Umidade")

fig_temperatura = px.line(df,
                          x='data_datetime',
                          y='Temperatura',
                          title="Temperatura por Data")
fig_temperatura.update_layout(xaxis_title="Data", yaxis_title="Temperatura")

fig_ph = px.line(df,
                 x='data_datetime',
                 y='pH',
                 title="pH por Data")
fig_ph.update_layout(xaxis_title="Data", yaxis_title="pH")

fig_nitrogenio = px.line(df,
                         x='data_datetime',
                         y='Nitrogênio',
                         title="Nitrogênio por Data")
fig_nitrogenio.update_layout(xaxis_title="Data", yaxis_title="Nitrogênio")

fig_fosforo = px.line(df,
                      x='data_datetime',
                      y='Fósforo',
                      title="Fósforo po Data")
fig_fosforo.update_layout(xaxis_title="Data", yaxis_title="Fósforo")

fig_potassio = px.line(df,
                       x='data_datetime',
                       y='Potássio',
                       title="Potássio por Data")
fig_potassio.update_layout(xaxis_title="Data", yaxis_title="Potássio")

#fig_calcio = px.line(df,
#                     x='data_datetime',
#                     y='calcio',
#                     title="Cálcio por Data")
#fig_calcio.update_layout(xaxis_title="Data", yaxis_title="Cálcio")

#fig_magnesio = px.line(df,
#                       x='data_datetime',
#                       y='magnesio',
#                       title="Magnésio por Data")
#fig_magnesio.update_layout(xaxis_title="Data", yaxis_title="Magnésio")

#fig_enxofre = px.line(df,
#                      x='data_datetime',
#                      y='enxofre',
#                      title="Enxofre por Data")
#fig_enxofre.update_layout(xaxis_title="Data", yaxis_title="Enxofre")

#---------------------------------
# Página
#---------------------------------

st.title(f"Coordenada: {f_coordenada}")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(fig_umidade)
    st.plotly_chart(fig_ph)
    st.plotly_chart(fig_fosforo)
    #st.plotly_chart(fig_calcio)
    #st.plotly_chart(fig_enxofre)

with col2:
    st.plotly_chart(fig_temperatura)
    st.plotly_chart(fig_nitrogenio)
    st.plotly_chart(fig_potassio)
    #st.plotly_chart(fig_magnesio)
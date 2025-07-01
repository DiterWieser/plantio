import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

#---------------------------------
# Dados
#---------------------------------

path_json = "plantio_refinado.json"
df = pd.read_json(path_json)

#---------------------------------
# Tratamento
#---------------------------------

df = df.T
df['coordenada_str'] = df['latitude'].astype(str) + ',' + df['longitude'].astype(str)

# Processamento provisório

coordenada_umidade = df.groupby('coordenada_str')[['umidade']].mean().reset_index()
coordenada_umidade = df.drop_duplicates(subset='coordenada_str')[['coordenada_str', 'latitude', 'longitude']].merge(coordenada_umidade, on='coordenada_str').reset_index()

#---------------------------------
# Gráficos
#---------------------------------

#fig_mapa_umidade = px.scatter_geo(coordenada_umidade,
#                                  lat='latitude',
#                                  lon='longitude',
#                                  scope='south america',
#                                  hover_name='coordenada_str',
#                                  size='umidade',
#                                  title="Umidade de cada área")

#---------------------------------
# Página
#---------------------------------

st.title("Mapa da Área de Plantio")

#st.plotly_chart(fig_mapa_umidade)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

#-----------------------------
#  Dados
#-----------------------------

path_padrao = "padrao.json"
padrao = pd.read_json(path_padrao)

path = "plantio_refinado.json"
df = pd.read_json(path)

#-----------------------------
#  Tratamento
#-----------------------------

padrao = padrao.T

df = df.T

df['coordenada'] = tuple((row['latitude'], row['longitude']) for _, row in df.iterrows())
df['coordenada_str'] = df['latitude'].astype(str) + ';' + df['longitude'].astype(str)

# Como tratar um string em datetime no pandas?
df["data_datetime"] = pd.to_datetime(arg=df['data_analise'], dayfirst='year') 

#-----------------------------
# Sidebar
#-----------------------------

st.sidebar.title("Filtros")

with st.sidebar:
    datas = df['data_analise'].unique()
    f_data = st.selectbox("Datas", datas)

query = '''data_analise in @f_data'''

df = df.query(query)

#-----------------------------
# Tabelas
#-----------------------------

#-----------------------------
#  Gráficos
#-----------------------------

fig_ph = px.bar(df,
                x='coordenada_str',
                y='pH',
                text_auto=True,
                title="pH do Solo")

fig_nitrogenio = px.bar(df,
                         x='coordenada_str',
                         y='nitrogenio',
                         text_auto=True,
                         title='Quantidade de Nitrogênio no Solo')

fig_fosforo = px.bar(df,
                     x='coordenada_str',
                     y='fosforo',
                     text_auto=True,
                     title="Quantidade de Fósforo no Solo")

fig_potassio = px.bar(df,
                      x='coordenada_str',
                      y='potassio',
                      text_auto=True,
                      title="Quantidade de Potássio no Solo")

fig_calcio = px.bar(df,
                    x='coordenada_str',
                    y='calcio',
                    text_auto=True,
                    title="Quantidade de Cálcio no Solo")

fig_magnesio = px.bar(df,
                      x='coordenada_str',
                      y='magnesio',
                      text_auto=True,
                      title="Quantidade de Magnésio no Solo")

fig_enxofre = px.bar(df,
                     x='coordenada_str',
                     y='enxofre',
                     text_auto=True,
                     title="Quantidade de Enxofre no Solo")

#-----------------------------
#  Pagina
#-----------------------------

st.title("Área de Plantio")

tab_area, tab_tabela = st.tabs(['Área', 'Tabela'])

with tab_area:
    st.title(f_data)
    
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(fig_ph)
        st.plotly_chart(fig_fosforo)
        st.plotly_chart(fig_calcio)
        st.plotly_chart(fig_enxofre)

    with col2:
        st.plotly_chart(fig_nitrogenio)
        st.plotly_chart(fig_potassio)
        st.plotly_chart(fig_magnesio)

with tab_tabela:
    st.title('Tabela')
    st.dataframe(df)
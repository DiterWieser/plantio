import pandas as pd

path_csv = "sensor_data.csv"
df = pd.read_csv(path_csv)

#-----------------------------
#  Tratamento
#-----------------------------

#df = df.T

df['coordenada'] = tuple((row['Latitude'], row['Longitude']) for _, row in df.iterrows())
df['coordenada_str'] = df['Latitude'].astype(str) + ';' + df['Longitude'].astype(str)

# Como tratar um string em datetime no pandas?
df["data_datetime"] = pd.to_datetime(arg=df['Data e Hora'], yearfirst=True) 


print(df)
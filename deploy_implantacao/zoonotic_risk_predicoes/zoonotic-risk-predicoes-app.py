# EN: Streamlit app for visualizing zoonotic risk predictions by farm
# PT: Aplicativo Streamlit para visualizar previsões de risco zoonótico por fazenda

import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# EN: Consume data from the FastAPI API
# PT: Consome os dados da API FastAPI
url = "https://vet-onehealth-data-science.onrender.com/predict"
response = requests.get(url)
data = response.json()

# EN: Convert JSON into a DataFrame
# PT: Converte o JSON em DataFrame
df = pd.DataFrame(list(data.items()), columns=["Farm", "Risk"])

# EN: Visualization
# PT: Visualização
st.title("Zoonotic Risk Predictions")
fig = px.bar(df, x="Farm", y="Risk", title="Predicted Risk by Farm")
st.plotly_chart(fig)

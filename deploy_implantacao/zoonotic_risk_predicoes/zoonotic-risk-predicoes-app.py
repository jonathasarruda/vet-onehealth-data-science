# EN: Streamlit app for visualizing zoonotic risk predictions by farm
# PT: Aplicativo Streamlit para visualizar previsões de risco zoonótico por fazenda

import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# EN: Base URL of the FastAPI API
# PT: URL base da API FastAPI
BASE_URL = "https://vet-onehealth-data-science.onrender.com/predict"

# EN: Select farm from dropdown
# PT: Seleciona a fazenda no menu suspenso
farm_choice = st.selectbox(
    "Choose a farm / Escolha uma fazenda",
    ["All", "Farm A", "Farm B", "Farm C"]
)

# EN: Build request depending on choice
# PT: Monta a requisição dependendo da escolha
if farm_choice == "All":
    response = requests.get(BASE_URL)
else:
    response = requests.get(f"{BASE_URL}?farm={farm_choice}")

data = response.json()

# EN: Convert JSON into DataFrame
# PT: Converte o JSON em DataFrame
df = pd.DataFrame(list(data.items()), columns=["Farm", "Risk"])

# EN: Visualization
# PT: Visualização
st.title("Zoonotic Risk Predictions")
fig = px.bar(df, x="Farm", y="Risk", title="Predicted Risk by Farm")
st.plotly_chart(fig)

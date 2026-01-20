# EN: Streamlit app for visualizing zoonotic risk predictions by farm
# PT: Aplicativo Streamlit para visualizar previsões de risco zoonótico por fazenda

import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({"Farm": ["A", "B", "C"], "Risk": [0.85, 0.40, 0.65]})

st.title("Zoonotic Risk Predictions")
fig = px.bar(df, x="Farm", y="Risk", title="Predicted Risk by Farm")
st.plotly_chart(fig)

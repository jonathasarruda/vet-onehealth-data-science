### Enunciado (EN/PT)  

**EN:** Given a table of veterinary predictions already obtained (zoonotic risk per farm), design a transversal deploy that documents, visualizes, exposes, and automates these results.  
**PT:** Dada uma tabela de previsões veterinárias já obtidas (risco zoonótico por fazenda), projete um deploy transversal que documente, visualize, exponha e automatize esses resultados.  

---

### Solução (Deploy sobre resultados já existentes)
#### 📘 Explicação técnica (Markdown/GitHub)
# One Health Predictions — Deploy

**EN:** This document shows how predictions are deployed across documentation, visualization, API, and automation.  
**PT:** Este documento mostra como previsões são implantadas nas camadas de documentação, visualização, API e automação.

---
  
# 📊 Interatividade (Streamlit/Plotly)

# Language: Python | Linguagem: Python
import streamlit as st
import pandas as pd
import plotly.express as px

# Example: mimicked predictions table
df = pd.DataFrame({
    "Farm": ["A", "B", "C"],
    "Risk": [0.85, 0.40, 0.65]
})

st.title("Zoonotic Risk Predictions")
fig = px.bar(df, x="Farm", y="Risk", title="Predicted Risk by Farm")
st.plotly_chart(fig)

# ⚙️ Paradigm | Paradigma
# EN: This code is declarative because it specifies what to render without manual drawing.
# PT: Este código é declarativo porque especifica o que renderizar sem desenhar manualmente.

---

# 🔗 Integração (FastAPI)

# Language: Python | Linguagem: Python
from fastapi import FastAPI

app = FastAPI()

# Mimicked predictions
predictions = {"Farm A": 0.85, "Farm B": 0.40, "Farm C": 0.65}

@app.get("/predict")
def get_predictions():
    return predictions

# ⚙️ Paradigm | Paradigma
# EN: This code is RESTful because it exposes resources via HTTP endpoints.
# PT: Este código é RESTful porque expõe recursos via endpoints HTTP.

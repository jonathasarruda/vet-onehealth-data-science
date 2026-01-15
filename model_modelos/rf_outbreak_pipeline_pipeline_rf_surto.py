## 📝 Question | Questão  
# EN: In a One Health dataset integrating cattle fever (animal), human influenza (human), and air pollution (environment), how to impute missing values, train a Random Forest classifier for outbreak risk, and evaluate performance with F1‑score using an SQL–Python–SQL pipeline?  

# PT: Em um conjunto de dados de Saúde Única integrando febre bovina (animal), influenza humana (humano) e poluição do ar (ambiental), como imputar valores ausentes, treinar um classificador Random Forest para risco de surto e avaliar o desempenho com F1‑score usando um pipeline SQL–Python–SQL?  

---

## 💬 Answer | Resposta  
# EN/PT: SQL → Python → SQL; imputation | imputação; Random Forest; F1‑score
  
# Language: Python | Linguagem: Python

# 🔬 One Health outbreak risk prediction | Predição de risco de surtos em Saúde Única
# 🧪 SQL–Python–SQL pipeline | Pipeline SQL–Python–SQL
# 🧪 Imputation + Random Forest + F1-score | Imputação + Random Forest + F1-score

# ⚙️ Paradigm | Paradigma
# EN: This code is imperative/procedural because it executes step by step, telling the computer what to do.
#     It also uses object-oriented elements: RandomForestClassifier is a class, and when we instantiate it,
#     we create an object (here called 'm') that can be trained with data and then used to make predictions.
# PT: Este código é imperativo/procedural porque executa passo a passo, dizendo ao computador o que fazer.
#     Também usa elementos orientados a objetos: o RandomForestClassifier é uma classe, e quando a instanciamos,
#     criamos um objeto (aqui chamado 'm') que pode ser treinado com dados e depois usado para fazer previsões.

# 📦 Import libraries | Importar bibliotecas
import sqlite3, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# 💾 Create in‑memory SQL database and insert sample data
# 💾 Criar banco de dados SQL em memória e inserir dados de exemplo
conn = sqlite3.connect(":memory:")
conn.executescript("""
CREATE TABLE data(id,fever,influenza,pollution,label);
INSERT INTO data VALUES
(1,38.5,1,70,0),
(2,NULL,0,90,1),
(3,39.2,1,110,1);
""")

# 📊 Load data into pandas and impute missing values
# 📊 Carregar dados no pandas e imputar valores ausentes
df = pd.read_sql("SELECT * FROM data", conn)
df["fever"] = df["fever"].fillna(df["fever"].mean())

# 🤖 Train Random Forest classifier
# 🤖 Treinar classificador Random Forest
m = RandomForestClassifier().fit(df[["fever","influenza","pollution"]], df["label"])

# 📈 Evaluate model with F1-score
# 📈 Avaliar modelo com F1-score
print(f1_score(df["label"], m.predict(df[["fever","influenza","pollution"]])))

### ✅ Expected Output | Saída Esperada
1.0

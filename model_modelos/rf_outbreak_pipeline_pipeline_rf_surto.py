## 📝 Question | Questão  

**EN:**  
In a One Health dataset integrating cattle fever (animal), human influenza (human), and air pollution (environment), how to impute missing values, train a Random Forest classifier for outbreak risk, and evaluate performance with F1‑score using an SQL–Python–SQL pipeline?  

**PT:**  
Em um conjunto de dados de Saúde Única integrando febre bovina (animal), influenza humana (humano) e poluição do ar (ambiental), como imputar valores ausentes, treinar um classificador Random Forest para risco de surto e avaliar o desempenho com F1‑score usando um pipeline SQL–Python–SQL?  

---

## 🗣️ Answer | Resposta  

**EN/PT:**  
SQL → Python → SQL; imputation; Random Forest; F1‑score.  

```python
import sqlite3, pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
conn=sqlite3.connect(":memory:")
conn.executescript("CREATE TABLE data(id,fever,influenza,pollution,label);"
                   "INSERT INTO data VALUES(1,38.5,1,70,0),(2,NULL,0,90,1),(3,39.2,1,110,1);")
df=pd.read_sql("SELECT * FROM data",conn)
df["fever"]=df["fever"].fillna(df["fever"].mean())
m=RandomForestClassifier().fit(df[["fever","influenza","pollution"]],df["label"])
print(f1_score(df["label"],m.predict(df[["fever","influenza","pollution"]]))) 

### ✅ Expected Output | Saída Esperada
1.0

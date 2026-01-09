# 📝 Question | Questão
# EN:  
# In cattle surveillance, how to impute missing temperatures by herd mean using an in‑memory SQL‑Python‑SQL pipeline and classify outbreak risk?

# PT:  
# Na vigilância bovina, como imputar temperaturas ausentes pela média do rebanho usando um pipeline SQL‑Python‑SQL em memória e classificar risco de surto?

# 🗣️ Answer | Resposta
# EN: Read SQL, impute herd mean in Python, write back, classify risk in SQL.

#  PT: Ler SQL, imputar média do rebanho em Python, gravar de volta e classificar risco em SQL.

import sqlite3, pandas as pd
conn = sqlite3.connect(":memory:")  # EN: in-memory DB | PT: banco em memória

# EN: create table with missing temps | PT: cria tabela com temperaturas ausentes
conn.executescript("CREATE TABLE cattle(id,herd,temp);"
                   "INSERT INTO cattle VALUES(1,1,38.5),(2,1,NULL),(3,2,39.2);")

df = pd.read_sql("SELECT * FROM cattle", conn)  # EN/PT: read table
df["temp"] = df.groupby("herd")["temp"].transform(lambda s: s.fillna(s.mean()))  # EN/PT: herd mean imputation
df.to_sql("cattle", conn, index=False, if_exists="replace")  # EN/PT: write corrected

# EN: classify risk by avg temp | PT: classifica risco pela média
print(pd.read_sql("SELECT herd,AVG(temp) AS avg,"
                  "CASE WHEN AVG(temp)>=39 THEN 'high' ELSE 'low' END risk "
                  "FROM cattle GROUP BY herd", conn))

## 📊 Expected Output | Saída Esperada

| herd | avg   | risk     |
|------|-------|----------|
| 1    | 38.5  | low      |
| 2    | 39.2  | high     |

### EN
- Herd 1 → average temperature = 38.5 → **low risk**  
- Herd 2 → average temperature = 39.2 → **high risk**

### PT
- Rebanho 1 → temperatura média = 38.5 → **baixo risco**  
- Rebanho 2 → temperatura média = 39.2 → **alto risco**

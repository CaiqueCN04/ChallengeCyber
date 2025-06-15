import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_PATH = "data/synthetic_data.csv"

# Verifica se o dataset existe
if not os.path.exists(DATA_PATH):
    print("❌ Dataset não encontrado. Execute gera_modelo.py primeiro.")
    exit()

# Carrega dados
df = pd.read_csv(DATA_PATH)

# Simula variável sensível (ex: grupo A/B)
df["grupo_simulado"] = ["A" if x % 2 == 0 else "B" for x in range(len(df))]

# Converte rótulo de risco para nome
df["risk_label"] = df["risk_level"].map({
    0: "muito baixo",
    1: "baixo",
    2: "moderado",
    3: "alto",
    4: "crítico"
})

# === FAIRNESS: Comparação por grupo ===
print("\n📊 Distribuição de risco por grupo_simulado:")
dist_grupo = df.groupby("grupo_simulado")["risk_level"].value_counts(normalize=True).unstack().fillna(0)
print(dist_grupo.round(3))

# === DIVERSIDADE: Verificar faixas de valor apostado ===
df["faixa_aposta"] = pd.cut(df["avg_bet_amount"], bins=[0, 30, 60, 90, 200], labels=["0-30", "31-60", "61-90", "91+"])

print("\n📊 Distribuição de risco por faixa de valor apostado:")
dist_aposta = df.groupby("faixa_aposta")["risk_level"].value_counts(normalize=True).unstack().fillna(0)
print(dist_aposta.round(3))

# === ALERTAS ÉTICOS ===
print("\n🔎 Análise ética automática:")

ALERTA_LIMIAR = 0.4
for grupo in dist_grupo.index:
    for nivel in dist_grupo.columns:
        if dist_grupo.loc[grupo, nivel] > ALERTA_LIMIAR:
            print(f"⚠️ ALERTA: Grupo {grupo} tem {dist_grupo.loc[grupo, nivel]*100:.1f}% de risco nível {nivel}")

print("\n✅ Auditoria finalizada.")

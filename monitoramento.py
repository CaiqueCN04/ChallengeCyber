import pandas as pd
import numpy as np
import os

DATA_PATH = "data/synthetic_data.csv"

if not os.path.exists(DATA_PATH):
    print("❌ Arquivo de dados não encontrado. Execute gera_modelo.py.")
    exit()

df = pd.read_csv(DATA_PATH)

# Métricas a monitorar
colunas_monitorar = ["daily_bets", "avg_bet_amount", "sessions_per_day", "time_spent_minutes"]

print("📊 MONITORAMENTO DE ANOMALIAS EM TEMPO REAL\n")

for coluna in colunas_monitorar:
    media = df[coluna].mean()
    desvio = df[coluna].std()
    limite_superior = media + 2 * desvio
    limite_inferior = media - 2 * desvio

    anomalias = df[(df[coluna] > limite_superior) | (df[coluna] < limite_inferior)]

    print(f"🔍 {coluna}: {len(anomalias)} possíveis anomalias detectadas.")
    if not anomalias.empty:
        print(anomalias[[coluna, "risk_level"]].head(3))
        print("...")

print("\n✅ Monitoramento concluído.")

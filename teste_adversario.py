import pandas as pd
import numpy as np
import pickle
import os

# === CONFIGURAÇÕES ===
modelo_path = "models/risk_model.pkl"

if not os.path.exists(modelo_path):
    print("❌ Modelo não encontrado. Execute gera_modelo.py primeiro.")
    exit()

with open(modelo_path, "rb") as f:
    model = pickle.load(f)

# === ENTRADA BASE (simulando um usuário realista) ===
entrada_base = {
    "daily_bets": 5,
    "avg_bet_amount": 80,
    "sessions_per_day": 3,
    "time_spent_minutes": 90,
    "lost_money_days": 12,
    "won_money_days": 6,
    "self_exclusion_attempts": 1,
    "account_age_days": 300
}

# === GERA VARIAÇÕES ADVERSARIAIS ===
percentuais = [-0.1, -0.05, 0, 0.05, 0.1]  # ±10%
variacoes = []

for db in percentuais:
    for amt in percentuais:
        for time in percentuais:
            var = entrada_base.copy()
            var["daily_bets"] = int(var["daily_bets"] * (1 + db))
            var["avg_bet_amount"] = var["avg_bet_amount"] * (1 + amt)
            var["time_spent_minutes"] = var["time_spent_minutes"] * (1 + time)
            variacoes.append(var)

# === PREDIÇÃO ===
df = pd.DataFrame(variacoes)
probas = model.predict_proba(df)
scores = [round(sum(i * p for i, p in enumerate(prob)) / (len(prob)-1), 3) for prob in probas]

df["predicted_risk"] = scores

# === ANÁLISE ===
print("\n📊 Avaliação adversarial — impacto de pequenas mudanças:")
print(df[["daily_bets", "avg_bet_amount", "time_spent_minutes", "predicted_risk"]])

print("\n🔍 Diferença máxima de risco: ", round(df["predicted_risk"].max() - df["predicted_risk"].min(), 3))

# === ALERTA ÉTICO ===
if df["predicted_risk"].max() - df["predicted_risk"].min() > 0.6:
    print("⚠️ ALERTA: Modelo altamente sensível a perturbações adversariais.")
else:
    print("✅ Modelo relativamente robusto a variações simples.")

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

os.makedirs("models", exist_ok=True)
os.makedirs("data", exist_ok=True)

n = 1000
df = pd.DataFrame({
    'daily_bets': np.random.poisson(5, n),
    'avg_bet_amount': np.random.normal(50, 20, n),
    'sessions_per_day': np.random.randint(1, 10, n),
    'time_spent_minutes': np.random.normal(90, 30, n),
    'lost_money_days': np.random.randint(0, 30, n),
    'won_money_days': np.random.randint(0, 30, n),
    'self_exclusion_attempts': np.random.binomial(2, 0.2, n),
    'account_age_days': np.random.randint(30, 1000, n),
})

# Criar rótulo sintético de risco
df['risk_level'] = pd.qcut(df['lost_money_days'] + df['daily_bets'], 5, labels=[0,1,2,3,4])
df.to_csv("data/synthetic_data.csv", index=False)

X = df.drop(columns=['risk_level'])
y = df['risk_level'].astype(int)

model = RandomForestClassifier()
model.fit(X, y)

with open("models/risk_model.pkl", "wb") as f:
    pickle.dump(model, f)

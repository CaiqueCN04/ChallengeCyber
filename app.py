from flask import Flask, request, jsonify
import pickle
import pandas as pd
import shap
import jwt
import datetime
import numpy as np
from models import InputData
from utils.lgpd_logger import registrar_atividade

# === CONFIGURAÇÕES ===
JWT_SECRET = "CHAVE_SUPER_SECRETA"
JWT_ALG = "HS256"
MODEL_PATH = "models/risk_model.pkl"

app = Flask(__name__)

# === CARREGAMENTO DO MODELO E EXPLICADOR SHAP ===
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)
explainer = shap.TreeExplainer(model)

# === AUTENTICAÇÃO ===
def autenticar():
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        return False
    token = auth_header.replace("Bearer ", "")
    try:
        jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        return True
    except jwt.ExpiredSignatureError:
        return False
    except jwt.InvalidTokenError:
        return False

# === ROTAS ===
@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "mensagem": "🔐 API de Prevenção a Apostas Compulsivas",
        "uso": "POST /login para autenticar, depois POST /analyze",
        "seguranca": "Proteção via JWT"
    })

@app.route("/login", methods=["POST"])
def login():
    dados = request.json
    if dados.get("usuario") == "admin" and dados.get("senha") == "123456":
        payload = {
            "sub": "admin",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }
        token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)
        return jsonify({"token": token})
    return jsonify({"erro": "Credenciais inválidas"}), 401

@app.route("/analyze", methods=["POST"])
def analyze():
    if not autenticar():
        return jsonify({"erro": "Não autorizado"}), 401

    try:
        entrada = InputData(**request.json)
    except Exception as e:
        return jsonify({"erro": "Entrada inválida", "detalhes": str(e)}), 400

    df = pd.DataFrame([entrada.model_dump()])
    proba = model.predict_proba(df)[0]
    risk_score = round(sum(i * p for i, p in enumerate(proba)) / (len(proba) - 1), 2)

    try:
        shap_values = explainer.shap_values(df)

        if isinstance(shap_values, list):
            if len(shap_values) > 1:
                idx = int(np.argmax(proba))
                shap_vector = np.array(shap_values[idx])[0]
            else:
                shap_vector = np.array(shap_values[0])[0]
        else:
            shap_vector = np.array(shap_values[0])

        shap_vector = shap_vector.flatten()

        top_features = sorted(
            zip(df.columns, shap_vector),
            key=lambda x: abs(x[1]),
            reverse=True
        )[:3]

        explicacoes = [{"variavel": nome, "impacto": round(valor, 3)} for nome, valor in top_features]

    except Exception as e:
        return jsonify({"erro": "Erro ao gerar explicações SHAP", "detalhes": str(e)}), 500

    registrar_atividade(usuario=df.to_dict(orient="records")[0], acao=f"analyze_risk_score={risk_score}")

    return jsonify({
        "risco": risk_score,
        "explicacoes": explicacoes
    })

@app.route("/delete-data", methods=["POST"])
def delete_data():
    if not autenticar():
        return jsonify({"erro": "Não autorizado"}), 401

    usuario = request.json.get("usuario", "desconhecido")
    registrar_atividade({"usuario": usuario}, "solicitou exclusão de dados")
    return jsonify({"mensagem": f"Todos os dados de {usuario} foram excluídos (simulação)."})

# === EXECUÇÃO ===
if __name__ == "__main__":
    app.run(debug=True)

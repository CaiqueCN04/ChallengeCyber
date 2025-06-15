# 🎯 Challenge CyberSecurity — Detecção de Apostas Compulsivas

Este projeto propõe uma solução inteligente e segura para detectar comportamentos compulsivos em apostas online, fornecendo alertas, explicações e integrando princípios éticos e legais (LGPD).

---

## 📁 Estrutura do Projeto

challengeCyberSecurity/
├── app.py # API principal com Flask
├── auditoria_etica.py # Verificação ética do modelo
├── gera_modelo.py # Script de criação do modelo ML
├── models/
│ └── risk_model.pkl # Modelo treinado
├── utils/
│ ├── crypto.py # Criptografia e segurança
│ ├── lgpd_logger.py # Registro e rastreabilidade (LGPD)
│ └── .fernet.key # Chave de criptografia
├── data/
│ └── synthetic_data.csv # Dados sintéticos para testes
├── logs/
│ └── atividade.log # Log de auditoria
├── models.py # Esquema de entrada com Pydantic
├── monitoramento.py # Monitoramento de atividades
├── teste_adversario.py # Testes de ataque adversarial
├── requirements.txt
└── readme.md


---

## ⚙️ Como Executar o Projeto

### 1. Criar ambiente virtual e instalar dependências

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1     # PowerShell no Windows
pip install -r requirements.txt
2. Gerar o modelo (caso ainda não exista)
bash
Copiar
Editar
python gera_modelo.py
3. Iniciar o servidor Flask
bash
Copiar
Editar
python app.py
🔐 Login e Autenticação JWT
Obter token de acesso
powershell
Copiar
Editar
$body = @{ usuario = "admin"; senha = "123456" } | ConvertTo-Json
$response = Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -Body $body -ContentType "application/json"
$token = $response.token
📊 Enviar dados para análise
powershell
Copiar
Editar
$body = @{
    daily_bets = 5
    avg_bet_amount = 200.0
    sessions_per_day = 3
    time_spent_minutes = 90.0
    lost_money_days = 4
    won_money_days = 1
    self_exclusion_attempts = 1
    account_age_days = 365
} | ConvertTo-Json -Depth 3

Invoke-RestMethod -Uri http://localhost:5000/analyze `
  -Method Post `
  -Headers @{ Authorization = "Bearer $token" } `
  -Body $body `
  -ContentType "application/json"
✅ Funcionalidades
🔍 Detecção de risco com modelo de machine learning

🔐 Autenticação JWT e proteção de endpoints

🧠 Explicabilidade com SHAP

🛡️ Criptografia e conformidade com LGPD

📁 Logs de uso e exclusão de dados

🧪 Testes de segurança adversarial

⚖️ Auditoria de vieses e ética em IA

📦 Tecnologias
Python 3.12

Flask

scikit-learn

SHAP

PyJWT

Pydantic

Cryptography (Fernet)

LGPD logger

👨‍💻 Integrantes
Caique Chagas – RM: 551943

Guilherme Dal Posolo Matheus – RM: 98694

Guilherme Faustino Vargas – RM: 98278

João Lucas Yudi Hedi Handa – RM: 98458

Ryan Perez Pacheco – RM: 98782


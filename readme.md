# Projeto: Detecção de Apostas Compulsivas 📘

## 📄 Descrição

Este projeto tem como objetivo criar uma solução baseada em inteligência artificial para identificar usuários com comportamentos de risco relacionados a apostas compulsivas. Ele utiliza um modelo preditivo para classificar o risco e fornece explicações interpretáveis com SHAP, além de boas práticas de cibersegurança.

---

## 👥 Integrantes

- Caique Chagas – RM 551943  
- Guilherme Dal Posolo Matheus – RM 98694  
- Guilherme Faustino Vargas – RM 98278  
- João Lucas Yudi Hedi Handa – RM 98458  
- Ryan Perez Pacheco – RM 98782  

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.10+
- Git

### Passos

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/challengeCyberSecurity.git
cd challengeCyberSecurity
Crie e ative o ambiente virtual:

bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate  # Windows
# ou
source venv/bin/activate  # Linux/macOS
Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Execute a aplicação:

bash
Copiar
Editar
python app.py
O serviço estará disponível em: http://localhost:5000

🧪 Exemplo de Requisição
powershell
Copiar
Editar
$body = @{
  "usuario" = "admin"
  "senha" = "123456"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -Body $body -ContentType "application/json"
$token = $response.token

$input = @{
  "daily_bets" = 5
  "avg_bet_amount" = 50.75
  "sessions_per_day" = 3
  "time_spent_minutes" = 120
  "lost_money_days" = 3
  "won_money_days" = 2
  "self_exclusion_attempts" = 1
  "account_age_days" = 200
  "ja_buscou_ajuda" = $false
  "uso_cartao_credito" = $true
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5000/analyze -Method Post -Headers @{ Authorization = "Bearer $token" } -Body $input -ContentType "application/json"
🔐 Segurança e Conformidade
✅ Recebimento e Processamento
Validação de entradas com Pydantic

Sanitização e checagem automática de tipos

Registro de logs com horário e atividade via lgpd_logger

Preparado para pipeline DevSecOps com análise estática (Bandit)

✅ Explicabilidade (XAI)
Explicações com SHAP integradas

Remoção de dados sensíveis nos retornos

Estrutura compatível com testes de robustez adversária

✅ Mitigação de Vieses
Dataset balanceado

Capacidade de auditoria (módulo auditoria_etica.py)

Representatividade considerada na base

✅ LGPD
Criptografia em repouso com Fernet (AES)

Logs com rastreabilidade

Preparado para consentimento explícito do usuário

✅ Segurança Geral
Autenticação via JWT com validade e verificação

Validação de token nos endpoints

Estrutura compatível com princípios de Zero Trust

✅ Design Ético
Transparência algorítmica com explicabilidade (SHAP)

Diretos do usuário respeitados (explicação + controle)

Política ética representada em código e logs

📊 Análise Estática com Bandit
A aplicação passou por uma análise estática com Bandit, que identificou boas práticas de segurança e pontos de melhoria:

✅ Relatório disponível em: /security/bandit-report.txt

Pontos identificados:

Uso do módulo pickle (seguro neste contexto)

Segredo JWT hardcoded (recomenda-se usar variável de ambiente)
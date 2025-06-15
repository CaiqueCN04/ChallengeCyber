Projeto: Detecção de Apostas Compulsivas
📘 Descrição
Este projeto tem como objetivo criar uma solução baseada em inteligência artificial para identificar usuários com comportamentos de risco relacionados a apostas compulsivas. Ele utiliza um modelo preditivo para classificar o risco e fornece explicações interpretáveis com SHAP, além de boas práticas de cibersegurança.

👥 Integrantes
Caique Chagas – RM 551943

Guilherme Dal Posolo Matheus – RM 98694

Guilherme Faustino Vargas – RM 98278

João Lucas Yudi Hedi Handa – RM 98458

Ryan Perez Pacheco – RM 98782

🚀 Como Executar o Projeto
Pré-requisitos
Python 3.10+

Git

1. Clone o repositório
bash
Copiar
Editar
git clone https://github.com/seu-usuario/challengeCyberSecurity.git
cd challengeCyberSecurity
2. Crie e ative o ambiente virtual
bash
Copiar
Editar
python -m venv venv
.\venv\Scripts\activate     # Windows
# ou
source venv/bin/activate    # Linux/macOS
3. Instale as dependências
bash
Copiar
Editar
pip install -r requirements.txt
4. Execute a aplicação
bash
Copiar
Editar
python app.py
O serviço estará disponível em: http://localhost:5000

🧪 Exemplo de Requisição PowerShell
powershell
Copiar
Editar
$body = @{
    "usuario" = "admin"
    "senha"   = "123456"
} | ConvertTo-Json

$response = Invoke-RestMethod -Uri http://localhost:5000/login -Method Post -Body $body -ContentType "application/json"
$token = $response.token

$input = @{
    "daily_bets"              = 5
    "avg_bet_amount"          = 50.75
    "sessions_per_day"        = 3
    "time_spent_minutes"      = 120
    "lost_money_days"         = 3
    "won_money_days"          = 2
    "self_exclusion_attempts" = 1
    "account_age_days"        = 200
    "ja_buscou_ajuda"         = $false
    "uso_cartao_credito"      = $true
} | ConvertTo-Json

Invoke-RestMethod -Uri http://localhost:5000/analyze -Method Post `
  -Headers @{ Authorization = "Bearer $token" } `
  -Body $input -ContentType "application/json"
🔐 Segurança e Conformidade
✅ Recebimento e Processamento
 Validação e sanitização de entradas

 Monitoramento de anomalias básicas

 Preparado para integração com pipeline DevSecOps

✅ Explicabilidade (XAI)
 Explicações com SHAP

 Limpeza dos dados explicativos sensíveis

 Preparação para adversarial robustness

✅ Mitigação de Vieses
 Dataset balanceado

 Possibilidade de auditoria

 Representatividade nos dados

✅ LGPD
 Criptografia aplicada ao armazenamento

 Rastreamento por logs

 Controle de consentimento do usuário

✅ Segurança Geral
 Autenticação JWT com tokens

 Proteção de endpoints

 Arquitetura preparada para Zero Trust

✅ Design Ético
 Transparência algorítmica

 Direitos do usuário respeitados

 Política ética definida


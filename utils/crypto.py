from cryptography.fernet import Fernet
import os

# Caminho da chave
KEY_PATH = "utils/.fernet_key"

# Gerar ou carregar chave criptográfica
def load_or_create_key():
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_PATH, "wb") as f:
        f.write(key)
    return key

FERNET_KEY = load_or_create_key()
fernet = Fernet(FERNET_KEY)

def criptografar_dados(dados: str) -> str:
    return fernet.encrypt(dados.encode()).decode()

def descriptografar_dados(dados: str) -> str:
    return fernet.decrypt(dados.encode()).decode()

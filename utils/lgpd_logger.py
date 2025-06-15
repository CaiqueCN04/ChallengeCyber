import logging
import os
from utils.crypto import criptografar_dados

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("lgpd_auditoria")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("logs/atividade.log")
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)

if not logger.hasHandlers():
    logger.addHandler(file_handler)

def registrar_atividade(usuario: dict, acao: str):
    dados = f"USUARIO: {usuario} - ACAO: {acao}"
    criptografado = criptografar_dados(dados)
    logger.info(criptografado)

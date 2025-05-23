from Encriptador import *
from Decriptador import *

import secrets
import os


nome_arquivo = r"AES_exercício\plaintext.txt"

chave = bytes([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])
iv = secrets.token_bytes(16)

encripta_arquivo(nome_arquivo, chave, iv)

#nome_arquivo_encriptado = r"C:\Users\claudio.barradas\Downloads\SegurancaInformacao-IFPR-2025\plaintextencriptado.enc"
#decriptador(chave, nome_arquivo_encriptado)
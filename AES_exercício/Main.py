from Encriptador import *
from Decriptador import *

import secrets

nome_arquivo = "/home/aluno/Downloads/SegurancaInformacao-IFPR-2025/AES_exercício/plaintext.txt"

chave = b'12345689abcdef'
iv = secrets.token_bytes(16)

encripta_arquivo(nome_arquivo, chave, iv)


#nome_arquivo_encriptado = "encriptado" + nome_arquivo + ".enc"
#decriptador(chave, nome_arquivo_encriptado)
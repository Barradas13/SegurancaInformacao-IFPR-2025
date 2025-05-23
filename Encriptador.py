from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

import os

def encrypt_aes(key: bytes, iv: bytes, plaintext: bytes) -> bytes:
    """
    Criptografa o texto usando AES no modo CBC.

    :param key: Chave de criptografia de 16, 24 ou 32 bytes.
    :param iv: Vetor de inicialização de 16 bytes.
    :param plaintext: Texto em claro a ser criptografado.
    :return: Texto cifrado.
    """
    # Criação do cifrador AES no modo CBC
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    # Criando o objeto de criptografia
    encryptor = cipher.encryptor()

    # Preenchimento do texto em claro para ajustar ao tamanho do bloco
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Criptografando o texto em claro
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()

    return ciphertext

def cria_arquivo(version, iv, cipher_text, arquivo_nome):
    IDENT       = b'ED'                 # 2 bytes
    VERSION     = bytes(version)         # 1 byte
    ALGO        = bytes([0x01])         # 1 byte (AES)
    MODE        = bytes([0x01])         # 1 byte (CBC)
    IV          = bytes(iv)     # 16 bytes: 0x00..0x0F
    RESERVED    = bytes(11)  # 11 bytes: 0x00..0x0F
    
    header = bytearray()
    
    header += IDENT
    header += VERSION
    header += ALGO
    header += MODE
    header += IV
    header += RESERVED

    
    with open(arquivo_nome + ".enc", "wb") as f:
        f.write(header + cipher_text)


def encripta_arquivo(arquivo, chave, iv):
    with open(arquivo, "rb") as f:

        arquivo_nome = os.path.basename(arquivo).split(".")[0]

        ciphered = encrypt_aes(chave, iv, f.read())
        cria_arquivo([0x01], iv, ciphered, arquivo_nome + "encriptado")
        
        
        
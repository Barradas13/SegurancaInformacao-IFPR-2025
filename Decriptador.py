from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

import os

def decrypt_aes(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
    """
    Descriptografa o texto cifrado usando AES no modo CBC.

    :param key: Chave de criptografia de 16, 24 ou 32 bytes.
    :param iv: Vetor de inicialização de 16 bytes.
    :param ciphertext: Texto cifrado a ser descriptografado.
    :return: Texto em claro.
    """
    # Criação do cifrador AES no modo CBC
    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv),
        backend=default_backend()
    )

    # Criando o objeto de descriptografia
    decryptor = cipher.decryptor()

    # Descriptografando o texto cifrado
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remoção do preenchimento
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

    return plaintext

def decriptador(chave, arquivo):
    with open(arquivo, "rb") as f:

        header = f.read(32)
        
        ident      = header[0:2]        # 2 bytes
        version    = header[2]          # 1 byte
        algo       = header[3]          # 1 byte
        mode       = header[4]          # 1 byte
        iv         = header[5:21]       # 16 bytes
        reserved = header[21:32]      # 11 bytes 
        
        ciphered = f.read()

        print(ciphered)

        plainText = decrypt_aes(chave, iv, ciphered)
        
        arquivo_nome = os.path.basename(arquivo).split(".")[0]

        with open("decriptado" + arquivo_nome + ".dec", "wb") as f:
            f.write(plainText)
            
        
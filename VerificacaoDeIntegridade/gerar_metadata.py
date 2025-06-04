from encrypt_aes import encrypt_aes
import secrets
import os
def gerar_metadata(arquivo_original: str, chave: bytes, arquivo_metadata: str = None) -> str:
    with open(arquivo_original, "rb") as f:
        conteudo = f.read()

    iv = secrets.token_bytes(16)

    ciphertext = encrypt_aes(chave, iv, conteudo)
    fingerprint = ciphertext[-16:]  # Últimos 16 bytes

    header = bytearray()
    header += b'CF'                     # Identificador (2 bytes)
    header += bytes([0x01])             # Versão (1 byte)
    header += bytes([0x01])             # Algoritmo AES (1 byte)
    header += bytes([0x01])             # Modo CBC (1 byte)
    header += iv                        # IV (16 bytes)
    header += fingerprint               # Fingerprint (16 bytes)
    header += bytes(11)                 # Reservado (11 bytes)

    if arquivo_metadata is None:
        base_name = os.path.basename(arquivo_original)
        arquivo_metadata = os.path.splitext(base_name)[0] + ".meta"

    with open(arquivo_metadata, "wb") as f:
        f.write(header)

    return arquivo_metadata
from .Encriptador import encrypt_aes

def verificar_integridade(arquivo_original: str, arquivo_metadata: str, chave: bytes) -> bool:
    """
    :param arquivo_original: Caminho do arquivo original
    :param arquivo_metadata: Caminho do arquivo de metadados
    :param chave: Chave AES usada na >>>geração<<<
    """

    with open(arquivo_metadata, "rb") as f:
        metadata = f.read(48)

    ident = metadata[0:2]
    version = metadata[2]
    algo = metadata[3]
    mode = metadata[4]
    iv = metadata[5:21]
    fingerprint_original = metadata[21:37]
    reserved = metadata[37:48]

    if ident != b'CF' or version != 0x01 or algo != 0x01 or mode != 0x01:
        raise ValueError("Arquivo de metadados inválido ou corrompido")

    with open(arquivo_original, "rb") as f:
        conteudo = f.read()

    ciphertext = encrypt_aes(chave, iv, conteudo)
    fingerprint_atual = ciphertext[-16:]

    print(fingerprint_original == fingerprint_atual)
    return fingerprint_original == fingerprint_atual
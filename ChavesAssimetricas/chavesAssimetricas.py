from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
import json
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature


padding_config = padding.PSS(
                              mgf=padding.MGF1(hashes.SHA256()),
                              salt_length=padding.PSS.MAX_LENGTH
                            )


def criarChavePrivadaPublica():
    private_key = rsa.generate_private_key(
                                                public_exponent=65537,
                                                key_size=3072,
                                                backend=default_backend(),
                                            )

    public_key = private_key.public_key()
    
    return private_key, public_key


def assinarMensagem(message, chavePrivada):
    signature = chavePrivada.sign(
                              message,
                              padding_config,
                              hashes.SHA256() # A função hash utilizada para gerar o resumo da mensagem
                            )

    signed_msg = {
              'message': list(message),
              'signature': list(signature),
             }

    msg_assinada = json.dumps(signed_msg)
    
    return msg_assinada


def verificarAssinatura(msg_assinada, chavePublica):
    signed_msg = json.loads(msg_assinada)

    message = bytes(signed_msg['message'])
    signature = bytes(signed_msg['signature'])

    try:
        chavePublica.verify(
                                signature,      # A assinatura a ser verificada
                                message,        # A mensagem original que foi assinada
                                padding_config, # Configuração de preenchimento PSS
                                hashes.SHA256() # A mesma função hash usada para assinar a mensagem
                            )
        return True
    except InvalidSignature:
        return False
from .Pagina import  *
import  flet

import secrets

iv = secrets.token_bytes(16)

print("Iniciando Flet App...")

criarPagina(iv)


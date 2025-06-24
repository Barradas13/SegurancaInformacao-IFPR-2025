# Define campos
IDENT       = b'CF'                 # 2 bytes
VERSION     = bytes([0x01])         # 1 byte
ALGO        = bytes([0x01])         # 1 byte (AES)
MODE        = bytes([0x01])         # 1 byte (CBC)
IV          = bytes(range(0x00, 0x10))     # 16 bytes: 0x00..0x0F
FINGERPRINT = bytes(range(0x10, 0x20))     # 16 bytes: 0x10..0x1F
RESERVED    = bytes(11)             # 11 bytes de 0x00


# Monta o header (48 bytes)
header = bytearray()
header += IDENT
header += VERSION
header += ALGO
header += MODE
header += IV
header += FINGERPRINT
header += RESERVED

# Salva no arquivo
with open("arquivo.meta", "wb") as f:
    f.write(header)
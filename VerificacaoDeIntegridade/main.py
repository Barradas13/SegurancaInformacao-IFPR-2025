nome_arquivo = "plaintext.txt"
chave = bytes([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4])  # 16 bytes


arquivo_meta = gerar_metadata(nome_arquivo, chave)
print(f"Arquivo de metadados gerado: {arquivo_meta}")


integro = verificar_integridade(nome_arquivo, arquivo_meta, chave)
print(f"Arquivo íntegro? {integro}")


with open(nome_arquivo, "ab") as f:
    f.write(b" MODIFICADO")

integro = verificar_integridade(nome_arquivo, arquivo_meta, chave)
print(f"Arquivo íntegro após modificação? {integro}")
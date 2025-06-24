#!/bin/bash
# Verifica se o volume foi montado corretamente
if [ ! -d "/host_files" ]; then
  echo "ERRO: Diretório /host_files não encontrado."
  echo "Execute o container com: -v /:/host_files ou -v ~/:/host_files"
  exit 1
fi

# Executa o aplicativo
python3 ./Main.py
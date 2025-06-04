# README - Projeto de Criptografia AES

## Sobre Criptografia Clássica

A criptografia clássica refere-se aos métodos de cifragem utilizados antes da era digital, incluindo:

- **Cifras de substituição**: Cada letra do texto é substituída por outra (ex: Cifra de César)
- **Cifras de transposição**: As letras são reorganizadas seguindo um padrão
- **Máquinas de criptografia**: Como a famosa Enigma usada na Segunda Guerra Mundial

Estes métodos foram a base para o desenvolvimento da criptografia moderna, mas possuem vulnerabilidades conhecidas e não são mais considerados seguros para proteção de dados digitais.

## Sobre o AES (Advanced Encryption Standard)

O AES é um padrão de criptografia simétrica adotado pelo governo dos EUA em 2001 e amplamente utilizado mundialmente:

- **Tipo**: Criptografia simétrica (mesma chave para cifrar e decifrar)
- **Tamanhos de chave**: 128, 192 ou 256 bits
- **Blocos**: Trabalha com blocos de 128 bits (16 bytes)
- **Modos de operação**: ECB, CBC, CTR, etc. (nosso projeto usa CBC)
- **Segurança**: Considerado extremamente seguro quando implementado corretamente

## Sobre Este Projeto

Este projeto implementa operações criptográficas usando AES-CBC (Cipher Block Chaining) em Python, com duas funcionalidades principais:

### 1. Criptografia/Descriptografia de Arquivos
- Cifra arquivos com AES-CBC e cabeçalho personalizado
- Gera arquivos com extensão `.enc`
- Permite descriptografar mantendo a estrutura original

### 2. Verificação de Integridade
- Gera arquivos de metadados (`.meta`) com fingerprint criptográfico
- Permite verificar se um arquivo foi modificado
- Usa os últimos 16 bytes do texto cifrado como assinatura

## Tecnologias Utilizadas
- Python 3.x
- Biblioteca `cryptography`
- Modo CBC com padding PKCS7
- Manipulação de arquivos binários

## Importante
Este projeto é para fins educacionais. Em aplicações reais:
- Nunca use chaves fixas como nos exemplos
- Gerar IVs aleatórios para cada operação
- Implementar gerenciamento seguro de chaves
- Considerar proteções adicionais contra ataques

## Estrutura do Projeto
```
/VerificacaoDeIntegridade
    ├── encrypt_aes.py   
    ├── gerar_metadata.py   
    ├── verificar_integridade.py      
    ├── main.py            
    └── plaintext.txt   
```

## Como Usar
Consulte os exemplos em `main.py` para ver como:
1. Criptografar arquivos
2. Descriptografar arquivos
3. Gerar metadados de verificação
4. Verificar integridade de arquivos
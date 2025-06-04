# README - Projeto de Criptografia AES

## Sobre o Repositório

Repositório para armazenar projetos e materiais da matéria de Segurança da Informação tida em 2025 no Instituto Federal do Paraná com o professor Thiago Berticelli Lo

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

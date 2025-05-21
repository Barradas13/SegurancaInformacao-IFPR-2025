from MatrizOperations import *

def fazChave(senha):
    return exponenciacaoMatriz([[1,1], [1,0]], senha)

def colocaNoIndice(matriz, i, v):
    if i % 4 == 1:
        matriz[0][0] = v
    elif i % 4 == 2:
        matriz[0][1] = v
    elif i % 4 == 3:
        matriz[1][0] = v
    else:
        matriz[1][1] = v

def cript(message, senha):

    res = []

    chave = fazChave(int(senha))
    atual = [[0, 0],[0, 0]]

    for i in range(1, len(message) + 1):

        colocaNoIndice(atual, i, ord(message[i - 1]))

        if i % 4 == 0:

            multiplicacao = multiplicaMatriz(chave, atual)

            res.append(multiplicacao[0][0])
            res.append(multiplicacao[0][1])
            res.append(multiplicacao[1][0])
            res.append(multiplicacao[1][1])


            atual = [[0,0],[0,0]]

        if i == len(message) and i % 4 != 0:
            
            c = i + 1
            
            while c % 4 != 0: 
                colocaNoIndice(atual, c, ord("*"))
                c += 1 
            
            multiplicacao = multiplicaMatriz(chave, atual)

            res.append(multiplicacao[0][0])
            res.append(multiplicacao[0][1])
            res.append(multiplicacao[1][0])
            res.append(multiplicacao[1][1])

    for i in res:
        print(i, end=" ")
    print()

    return res

def decript(message, senha):
    chave = fazInversa(fazChave(int(senha)))
    atual = [[0, 0],[0, 0]]
    
    res = []
    
    message = message.split(" ")
    
    for i in range(1, len(message) + 1):
        print("msg", message[i-1], i)
        colocaNoIndice(atual, i, int(message[i - 1]))
        
        if i % 4 == 0:
            multiplicacao = multiplicaMatriz(chave, atual)

            print(multiplicacao)

            res.append(multiplicacao[0][0])
            res.append(multiplicacao[0][1])
            res.append(multiplicacao[1][0])
            res.append(multiplicacao[1][1])


            atual = [[0,0],[0,0]]

    return res
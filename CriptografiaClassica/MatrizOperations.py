#CODE RELATED TO OPERATIONS IN MATRIZ
def criaMatriz(n, m):
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(m):
            matriz[i].append(0)

    return matriz

def imprimeMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()

def multiplicaVetores(vet1, vet2):
    soma = 0

    for i in range(len(vet1)):
        soma += vet1[i] * vet2[i]
        
    return soma

def transpostaMatriz(matriz):
    matrizReturn = criaMatriz(len(matriz[0]), len(matriz))

    for i in range(len(matriz[0])):
        for j in range(len(matriz)):
            matrizReturn[i][j] = matriz[j][i]

    return matrizReturn

def multiplicaMatriz(mat1, mat2):
    mat2T = transpostaMatriz(mat2)
    mat3 = criaMatriz(len(mat1), len(mat2T))

    j = 0
    i = 0

    while j < len(mat1) and i != len(mat2[0]):
        mat3[i][j] = multiplicaVetores(mat1[i], mat2T[j])
        if i + 1 >= len(mat1):
            i = 0
            j += 1
        else:
            i += 1

    return mat3

def transformaNumeroBinario(n):
    binario = ""
    
    while n >= 1:
        resto = n % 2
        #print(resto)
        if resto == 0:
            binario = '0' + binario
        else:
            binario = '1' + binario
        n = int(n/ 2)

    return binario

#quero saber o n-ézimo elemento da fibonnaci de forma FAST
def exponenciacaoMatriz(matriz, n):

    binario = transformaNumeroBinario(n)
    
    #Agora dividimos para conquistar, fazemos o valor de cada mod da exponenciação por partes
    #E MULTIPLICAMOS E ENTÃO SOMENTE FAZEMOS O MOD FINAL

    lista = [matriz for i in binario]

    for i in range(len(binario) -1, -1, -1):
        if i != len(binario) -1:
            lista[i] = multiplicaMatriz(lista[i + 1], lista[i + 1])

    for i in range(len(binario)):
        if binario[i] == "1":
            matriz = multiplicaMatriz(matriz, lista[i])


    return matriz

def fazInversa(matriz):
    determinante = matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]

    return [[matriz[1][1] / determinante, -matriz[0][1]/determinante], [ -matriz[1][0]/determinante, matriz[0][0]/determinante]]


def imprimeMatriz(matriz):
    for i in matriz:
        for j in i:
            print(j, end=" ")
        print()
def gerarMatriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def printarMatriz(matriz):
    for i in range(len(matriz)):
        linha = matriz[i]
        print(linha)

def contraDiagonal(matrizQuadrada):
    #IMPORTANTE: quando a matriz recebe matrizQuadrada, a variavel matriz não copia e sim aponta para o mesmo objeto na memoria que matrizQuadrada
    matriz = matrizQuadrada #basicamente esta linha é inutil, mas é importante saber o por que
    if len(matriz[0]) == len(matriz):
        for i in range(len(matriz)):
            colunaDiagonal = len(matriz)-i-1 #colocamos -1 pois a linha 17 começa com "i=0" e termina em i=4, se o parametro for uma matriz de tamanho 5x5
            matriz[i][colunaDiagonal]=1
        return matriz
    else:
        print('Não é uma matriz quadrada')

def diagonal(matrizQuadrada):
    matriz = matrizQuadrada
    if len(matriz[0]) == len(matriz):
        for i in range(len(matriz)):
            matriz[i][i]=1
        return matriz
    else:
        print('Não é uma matriz quadrada')


def matrizTransposta(matrizQuadrada):
    # Esta função funciona porque as linhas 61 e 62 geram os seguintes números:
    # (1,0) ; (2,0)(2,1) ; (3,0)(3,1)(3,2) ; (4,0)(4,1)(4,2)(4,3)
    # que atendem os requisitos e são eficientes
    for i in range(len(matrizQuadrada)):
        for j in range(i): #só começa quando i for igual a 1 
            aux = matrizQuadrada[i][j]
            matrizQuadrada[i][j] = matrizQuadrada[j][i]
            matrizQuadrada[j][i] = aux
    return matrizQuadrada

def xadrez(matrizQuadrada):
    #temos os casos
    #(0,0)=preto -> (0,1)=branco
    #(1,0)=branco -> (1,1)=preto
    for i in range(len(matrizQuadrada)):
        for j in range(len(matrizQuadrada[0])):
            if i%2 == j%2:
                matrizQuadrada[i][j]=0
            else:
                matrizQuadrada[i][j]=1
    return matrizQuadrada
        
teste = gerarMatriz(8,8)
# printarMatriz(teste)
# contra_diagonal = contraDiagonal(teste)
# diagonal_ = diagonal(teste)
# print('\n\n')
# printarMatriz(contra_diagonal)
# print('\n\n')
# printarMatriz(diagonal_)
# print('\n\n')
printarMatriz(teste)
print('\n')
printarMatriz(xadrez(teste))



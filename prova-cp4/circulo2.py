import matplotlib.pyplot as plt

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

teste= gerarMatriz(50,50)

def padrao_circulo(matriz):
    """
    Cria uma matriz quadrada n x n com padrão de círculo.
    Retorna a matriz (lista de listas) e mostra a imagem.
    """
    # centro e raio
    c = (len(matriz) - 1) / 2
    r = (len(matriz) - 1) / 2

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            dist2 = (i - c) ** 2 + (j - c) ** 2
            if dist2 <= r ** 2:
                matriz[i][j] = 1  # dentro do círculo

    plt.imshow(matriz, 'hot')
    plt.show()

    return matriz

# Exemplo
matriz_circulo = padrao_circulo(teste)
printarMatriz(teste)

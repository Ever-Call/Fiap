import matplotlib.pyplot as plt

def gerarMatriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

matriz= gerarMatriz(50,50)

def padrao_circulo(n):
    """
    Cria uma matriz quadrada n x n com padrão de círculo.
    Retorna a matriz (lista de listas) e mostra a imagem.
    """
    matriz = []
    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)  # começa tudo com 0
        matriz.append(linha)

    # centro e raio
    c = (n - 1) / 2
    r = (n - 1) / 2

    for i in range(n):
        for j in range(n):
            dist2 = (i - c) ** 2 + (j - c) ** 2
            if dist2 <= r ** 2:
                matriz[i][j] = 1  # dentro do círculo

    plt.imshow(matriz, cmap="gray", interpolation="nearest")
    plt.axis("off")
    plt.show()

    return matriz

# Exemplo
matriz_circulo = padrao_circulo(50)

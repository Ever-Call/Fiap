def media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma/len(lista)
    return media


numeros = [10,2,3,4,5]
resultado = media(numeros)
print(resultado)


def qtdPares(lista):
    i=0
    for num in lista:
        if num %2 == 0:
            i+=1
    return i

pares = qtdPares(numeros)
print(pares)


def achar_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i]>maior:
            maior= lista[i]
            indice_maior = i
    return indice_maior
carros = ['up','gol','polinho','uno','celta']
precos = [10,20,1000000,100,200]
indice = achar_maior(precos)
veiculoMaisCaro = f'{carros[indice]} R${precos[indice]}'
print(veiculoMaisCaro)
'''ano = input("Diga seu ano de nascimento: ")
while not ano.isnumeric():
    ano = input("Diga seu ano de nascimento: ")
ano = int(ano)

vinho_1 = 'Pérgola'
vinho_2 = 'Sangue de Boi'
vinho_3 = 'Cantinho do Vale'
preco_1 = 10
preco_2 = 20
preco_3 = 30
qtd_1 = 0
qtd_2 = 0
qtd_3 = 0

idade = 2025 - ano
if idade < 18:
    print("Que feioooo, vô conta p sua mãe!🐱‍🚀🤬")
else:
    endereco = input("Diga seu endereço: ")
    valor_total = 0
    while True:
        escolha = input(f"Essas são nossas opções:\n{vinho_1} - {preco_1}\n"
                        f"\n{vinho_1} - {preco_1}\n{vinho_1} - {preco_1}\n"
                        f"Qual você quer?\n->")
        while not (escolha == vinho_1 or escolha == vinho_2 or escolha == vinho_3):
            print(f"{escolha} não é uma opção válida!")
            escolha = input(f"Essas são nossas opções:\n{vinho_1} - {preco_1}\n"
                            f"\n{vinho_1} - {preco_1}\n{vinho_1} - {preco_1}\n"
                            f"Qual você quer?\n->")
        qtd = input(f"Quantas garrafas de {escolha} você quer?\n->")
        while not qtd.isnumeric():
            print("Inválido!")
            qtd = input(f"Quantas garrafas de {escolha} você quer?\n->")
        qtd = int(qtd)
        if escolha == vinho_1:
            preco = preco_1
            qtd_1 += qtd
        elif escolha == vinho_2:
            preco = preco_2
            qtd_2 += qtd
        else:
            preco = preco_3
            qtd_3 += qtd
        valor_total += qtd*preco
        continuar = input("Você quer continuar comprando? (s/n)\n->")
        while not (continuar == 's' or continuar == 'n'):
            continuar = input("Você quer continuar comprando? (s/n)\n->")
        if continuar == 'n':
            break
    frete = 10
    if valor_total >= 500:
        print("Frete Grátis!")
        frete = 0
    valor_total += frete
    print(f"Obrigado por comprar aqui! Você comprou: \n{qtd_1} - {vinho_1}"
          f"\n{qtd_2} - {vinho_2}\n{qtd_3} - {vinho_3}\nTotalizando R${valor_total:.2f}"
          f" e seu pedido será entregue em {endereco}.")

vogais = 0
for char in 'danilo':
    if char in ['a','e','i','o','u']:
        vogais += 1
print(vogais)

for i in range(10):
    print(i)

for i in range(1,10,3):#ini,fim,passo
    print(i)

for i in range(20,10,-2):
    print(i)

for i in range(10):
    print(i)
    i = 0
    print(i)

for i in range(1,11):
    print(f"Tabuada do {i}:")
    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
    print()
i = 1
while i < 11:
    j = 1
    print(f"Tabuada do {i}:")
    while j < 11:
        print(f"{i}*{j} = {i * j}")
        j += 1
    i += 1
    print()

lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    print(elem)
print()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    print(elem)
print()
for i in range(len(lista)):
    print(f"lista[{i}] = {lista[i]}")

lista = [3,True,1.5,'danilo',[]]
for elem in lista:
    elem = 1
print(lista)
for i in range(len(lista)):
    lista[i] = 1
print(lista)

profs = ['Danilo','André','Gabi','Celso','Yan','Lucas','Luís']
materias = ['Python','Historinha','Sw&TX','Matemática','Edge','Front','Web']
for i in range(len(profs)):
    print(f"O/a prof {profs[i]} dá {materias[i]}")

alunos = ['Lucas Sena','Rhariel','Sara','Isabela','Lucas Zago']
notas = [8,8.5,6,4,1]

for i in range(len(alunos)):
    if notas[i] >= 6:
        print(f"{alunos[i]} foi aprovado/a")
    else:
        print(f"{alunos[i]} foi reprovado/a")

#Exercício 1 - contar a quantidade de numeros pares na lista
#Exercício 2 - Calcular a soma dos elementos da lista
#Exercício 3 - calcular a media dos elementos da lista
numeros = [90,7,3,5,2,1,8,6,0,4]
pares = 0
for num in numeros:
    if num % 2 == 0:
        pares += 1
pares = 0
for i in range(len(numeros)):
    if numeros[i] % 2 == 0:
        pares += 1
#ERRADO
pares = 0
for i in numeros:
    if numeros[i]%2 == 0:
        pares += 1

pares = 0
for numero in numeros:
    if numeros[numero]%2 == 0:
        pares += 1

numeros = [90,7,3,5,2,1,8,6,0,4]
soma = 0
for num in numeros:
    soma += num
print(soma)

soma = 0
for i in range(len(numeros)):
    soma += numeros[i]
print(soma)
media = soma/len(numeros)
#Errado!
soma = 0
for i in range(numeros):
    soma += numeros[i]
print(soma)

lista = []
lista.append(349)
print(lista)
lista.append(67)
print(lista)
lista.append(765)
print(lista)
lista = []
i = 0
while i < 10:
    num = input(f"Diga o {i+1}º numero: ")
    if not num.isnumeric():
        num = input(f"Diga o {i+1}º numero: ")
        continue
    num = int(num)
    lista.append(num)
    i+=1
    print(lista)

lista = []
for i in range(10):
    num = input(f"Diga o {i+1}º numero: ")
    while not num.isnumeric():
        num = input(f"Diga o {i+1}º numero: ")
    num = int(num)
    lista.append(num)
    print(lista)

a = input()
b = input()
c = input()

maior = a
if b > maior:
    b = a
if c > maior:
    c = maior
if d > maior:
    d = maior

lista = [7,3,8,5,2,0,9,6,10,4]
maior = lista[0]
for num in lista:
    print(f"Vou testar se {num} > {maior}")
    if num > maior:
        print(f"Deu certo, vou trocar {maior} por {num}")
        maior = num
print(f"O maior numero em {lista} é {maior}")
'''

preco = [600,50,80,1000000,5]
carros = ['Mustang','up','gol','POLINHO TURBÃO MANUAL😈','uno']
indice_maior = 0
maior = preco[0]
for i in range(len(preco)):
    #print(f"Vou testar se {preco[i]} > {maior}")
    if preco[i] > maior:
        #print(f"Deu certo, vou trocar {maior} por {preco[i]}")
        maior = preco[i]
        indice_maior = i
print(f"O carro mais caro é o {carros[indice_maior]}")
















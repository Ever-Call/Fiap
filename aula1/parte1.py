vogais = 0
for variavel in 'danilo':
    print(variavel)
    if variavel in ['a','e','i','o','u']:
        vogais += 1

print(vogais)

lista = [3, True, 7, 2, 'nome',[]]
for eles in lista:
    print(eles)
print(eles)
for i in range(len(lista)):
    print(lista[i])
    for eles in lista:
        eles = 1
        print(eles)
print(lista)
for i in range(len(lista)):
    lista[i] = 1
print(lista)

lista = [3, True, 7, 2, 'nome',[]]
for i in range(len(lista)):
    print(f'lista[{i}]= {lista[i]}')

numeros = [5,1,7,9,0,2]
print(numeros)
soma = 0
for num in numeros:
    soma+=num
print(soma)

soma=0
for i in range(len(numeros)):
    soma+= numeros[i]
print(soma)

soma =0 
for i in numeros: #este codigo esta certo, mas fica confuso por causa do i, que geralmente é usado como indice
    soma+=i
print(soma)

soma = 0
for i in numeros: #codigo errado!!!
    break #tire o break para entender
    soma += numeros[i]

# soma = 0
# for i in range(numeros):
#     soma += numeros[i]

alunos = ['Lucas Sena', 'Vinicius','Matheus Santos','Leandro Afonso']
notas = [2,6,8,5]
for notas in notas:
    if notas>=6:
        print('passou com {nota}')

notas = [2,6,8,5]
    
for i in range(len(notas)):
    if notas[i]>=6:
        print(f"O {alunos[i]} passou com {notas[i]}")
##########################################################################    
def verifica_numero(msg):
    numero = input(msg)
    while not numero.isnumeric():
        numero = input(msg)
    numero = int(numero)
    return numero # 'numero' não existe fora da função!!

qtd = verifica_numero('Quantos numeros voce vai colocar na lista?\n->')
ano = verifica_numero('Diga o seu ano de nascimentos: ')


lista= []
while len(lista)<qtd: # como a lista está vazia ela começa com 0, por isso adicionamos 1
    num = verifica_numero(f"Diga o {len(lista)+1}º numero:")
    lista.append(num)
    print(lista)


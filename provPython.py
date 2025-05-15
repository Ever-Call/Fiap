###### Codigo incompleto
# ano =input("Diga seu ano de nascimento: ")
# while not ano.isnumeric(){
#     ano = input("Diga seu ano de nascimento")
# }
# ano = int(ano)

# idade = 2025-ano
# vinho_1='Pergola'
# vinho_2= 'Saque'
# vinho_3 = 'Vinho forte'
# preco_1=10
# preco_2=20
# preco_3=30

# if idade<18:
#     print('Vá embora')
# else:
#     while true:
#     endereco = input(Diga seu enderco: )
#     escolha = input(f'Essas são nossas oções\n{vinho_1} - {preco_1}\n{vinho_2} - {preco_2}\n{vinho_3} - {preco_3}\nQual você quer?')
#     qtd = input(f"Quantas garrafas de {escolha} você quer?\n")
#     if escolha == vinho_1:
#         preco = preco_1
#         qtd_1+=qtd
#     elif escolha == vinho_2:
#         preco = preco_2
#         qtd_2 = qtd
#     else:
#         preco = preco_3
#         qtd_3 = qtd
#     continuar = input("Você quer continuar comprando? (s/n)\n>")
#     while not (continuar == 's' or continuar == 'n'):
#         continuar = input('Você quer continuar comprando? (s/n)\n>')
#     if continuar == 'n':
#         break

#     frete = 10
#     if valor_total >=500:
#         print('Frete grátis!')
#         frete = 0
#     print(f"Obrigado por comprar aqui!. Você comprou: \n{qtd_1}-{vinho_1}"
#         f"\n{qtd_2}-{vinho_2}\n{qtd_3}-{vinho_3}\nTotalizando R${valor_total} reais"
#         f"\ne seu pedido será entregue no endereço: {enderco}")

# vogais = 0
# for char in 'danilo':
#     if char in ('a','e','i','o','u'):
#         vogais+=1
# print(vogais)

#media dos numeros no arrays
#no mesmo array, contar a quantidade de pares
# numeros = [9,7,3,5,2,1,8,6,0,4]
# print(len(numeros))#retorna 10
# pares = 0
# for num in numeros:
#     if num%2 ==0:
#         pares +=1

# soma = 0
# for i in range(len(numeros)):
#     soma += numeros[i]
#     print(i) # i começa do 0
# print(soma)

# print(i)
# lista = []
# lsita.append(349)
# print(lista)
# lista.append(67)
# print(lista)
# lista.append(765)
# print(lista)

preco = [600,50,880,100,5]
carros = ['mustang','up','gol','POLINHO','uno']
indicie_maior = 0
maior = preco[0]
for i in range(len(preco)):
    if preco[i]>maior:
        maior = preco[1]
        indicie_maior = i
print(f'O carro mais caro é o {carros[indicie_maior]}')

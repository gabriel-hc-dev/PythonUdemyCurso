#Strings iteráveis...
#Cada letra tem um índice (positivo ou negativo)

# nome = 'Gabriel'
# print(nome[1])
# print(nome[-6])
# print(10*'-')
# print('l' in nome)
# print('Gab' not in nome)

nome = input("Digite seu nome: ")
encontrar = input("Digite o que quer encontrar: ")
if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}.')
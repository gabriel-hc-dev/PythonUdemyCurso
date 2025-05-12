#A função input faz com que o usuário interaja.
#Você pode coletar dados dessa forma.
nome = input('Qual o seu nome? ')
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
int_n1 = int(n1)
int_n2 = int(n2)
soma = int_n1 + int_n2
print(f'O seu nome é {nome=}\nA soma dos números é {soma}')
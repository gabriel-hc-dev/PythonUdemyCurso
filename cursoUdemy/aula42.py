#Operador lógico 'not'
#Inverte operações (not true = False), por exemplo.

senha = input('Senha: ')

if not senha:
    print('Senha incorreta.')
else:
    print('Você entrou no sistema.')

print('Bloco fora do if.')
print(not 1)
print(not 0)
print(not '')
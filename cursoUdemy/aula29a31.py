nome = 'Gabriel Henrique'
altura = 1.86
peso = 70
imc = peso / (altura ** 2)

print('Olá,', nome, '.\nVocê tem ', altura, ' de altura, e tem ', peso, ' quilogramas.')
print('Seu IMC é: ', imc)

#Formatação de strings - f-strings
linha_1 = f'{nome} tem {altura:,.3f} de altura'
linha_2 = f'pesa {peso} quilos e seu imc é de {imc:.2f}'
print(linha_1)
print(linha_2)
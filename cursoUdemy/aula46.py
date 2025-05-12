# Fatiamento de Strings
var = 'Olá mundo!'
# Geralmente, o índice final não é incluído (depois dos 2 pontos)
# O espaço é um caracter
print(var[1:5])
#Apesar da string ter 10 caracteres, ela termina no índice 9, pois começa a contar no 0.
print(len(var))
#O terceiro "dois pontos", é o passo, de quanto em quanto que pula. (se ele for negativo, inverte a string)
print(var[0:10:2])
print(var[::-1])
#Precedência de operadores
#1. Parênteses
#2. Potenciação
#3. Multiplicação, divisão (inteira) e módulo
#4. Soma e Subtração

c1 = 1 + 1 ** 5 + 5
print(c1)
#Realiza-se 1 a quinta primeiro, e depois soma.

c2 = (1+1) ** (5 + 5)
print(c2)
#Realiza-se o parenteses primeiro.
#Depois a potência
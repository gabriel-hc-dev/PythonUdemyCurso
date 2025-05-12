#Formatação de strings com o método format.
a = 'A'
b = 'B'
x = 1.1
strings = 'a = {nome1} \nb = {nome2} \nx = {num3:.3f}'
formato = strings.format(
    nome1 = a, nome2 = b, num3 = x)
print(formato)
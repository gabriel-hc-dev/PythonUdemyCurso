# Interpolação de String
# %s - string / %f - float / %d %e %i - int / %x ou %X - hexadecimal

nome = 'Gabriel'
preco = 1000.983791018272
var = '%s, o preço é de R$%.2f' %(nome, preco)
print(var)

#Ex Hexadecimal
print('O hexadecimal de %d é %04x' % (12000, 12000))
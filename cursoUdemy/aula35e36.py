#Continuação if, elif, else

condicao1 = True
condicao2 = True
condicao3 = True
condicao4 = True


#Sendo assim, com o elif, apenas uma condição será executada
#Sendo essa, a primeira a aparecer no código para o interpretador.
#Para termos mais de uma execução, usa-se um if encadeado (if, if, if, if)
if condicao1:
    print("Esse é o bloco da primeira condição.")
elif condicao2:
    print("Esse é o bloco da segunda condição.")
elif condicao3:
    print("Esse é o bloco da terceira condição.")
elif condicao4:
    print("Esse é o bloco da quarta condição.")
else:
    print("Nenhuma condição foi satisfeita.")
if 10 == 10:
    print("Outro bloco de if.")
print("Essa parte está fora do if.")
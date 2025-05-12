#Operador and (e)
#Quando utiliza ele, todas as condições precisam ser verdadeiros.
#Se algo for falso, a expressão inteira será avaliada ali.
#Falsy em python: 0, 0.0, '' e False
#O valor None não representa nenhum valor

#Avaliação de curto circuito
senha = input('Senha: ') or 'Sem senha'
print('A senha digitada foi:', senha)

entrada = input("[E]ntrar / [S]air: ")
senha1 = input('Senha: ')
senha_permitida = senha1
if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Seja bem vindo!')
else:
    print('Você saiu do sistema.')


# Verifica se há erros de digitação no CPf 
def verificacao_cpf():
    global cpf, cpf_numero_digito, cpf_inteiro, erro
    cpf = input('Digite o seu CPF: ').strip()
    if cpf.count('-') > 1 or cpf.count('.') > 2:
        print('excesso de "." ou "-"')
        erro = 1
    else:
        erro = 0
    cpf = cpf.split('.')
    cpf = ''.join(cpf)
    if not '-' in cpf:
        cpf = list(cpf)
        cpf.insert(-2, '-')
        cpf = ''.join(cpf)
    cpf_numero_digito = cpf.split('-')
    cpf_inteiro = ''.join(cpf_numero_digito)
    if cpf_inteiro == '':
        print('Campo Vazio')
    elif not cpf_inteiro.isnumeric():
        print('Tipos de caracteres não aceitos')
    elif len(cpf_inteiro) != 11:
        print('Quantidade de caracteres inválidos')
        
        
def continua(a):
    global x 
    while a not in 'SN':        
        a = input('Deseja validar outro CPF? [S/N] ').strip().upper()
        if a not in 'SN':
            print('Erro, Digite um comando válido')
            continue
        if a != 'S':
            print('Programa Finalizado com Sucesso')
            x= 'fechar programa'
            return('x')                            
        print('Digite somente, "S" para continuar e "N" para fechar o programa')        
                
                
x ='a'
a ='a'
while x != 'fechar programa':
    verificacao_cpf()
    while not cpf_inteiro.isnumeric() or '' or len(cpf_inteiro) != 11 or erro == 1:
        verificacao_cpf()

    cpf_numero = cpf_numero_digito[0]
    cpf_digito = cpf_numero_digito[1]

    cont = 10
    soma = 0
    for numero in cpf_numero:
        soma += int(numero) * cont
        cont -= 1

    verifica_digito1 = 11 - (soma % 11)
    if verifica_digito1 > 9:
        resultado_digito1 = 0
    else:
        resultado_digito1 = verifica_digito1

    if resultado_digito1 != int(cpf_digito[0]):
        print('CPF INVÁLIDO')
        print(f'Para o numero de CPF digitado o 1º número do digito deveria ser "{resultado_digito1}"')
        print(f'Porém, o número digitado foi {cpf_digito[0]}')
        print()
        continua(a)
    else:
        cpf_num_dig1 = list(cpf_numero)
        cpf_num_dig1.append(cpf_digito[0])

        cont = 11
        soma = 0
        for numero in cpf_num_dig1:
            soma += int(numero) * cont
            cont -= 1

        verifica_digito2 = 11 - (soma % 11)
        if verifica_digito2 > 9:
            resultado_digito2 = 0
        else:
            resultado_digito2 = verifica_digito2

        if resultado_digito2 != int(cpf_digito[1]):
            print('CPF INVÁLIDO')
            print(f'Para o numero de CPF digitado, o 2º número do digito  deveria ser "{resultado_digito2}"')
            print(f'Porém, o número digitado foi "{cpf_digito[1]}"')
            print()
            continua(a)
        else:
            print(f'{cpf} é um CPF válido')
            print()
            continua(a)
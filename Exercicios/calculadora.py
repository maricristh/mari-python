#calculadora - 18 jan 2023


while True: #loop que fica executando ate eu sair
    
    numero1 = input("Digite o primeiro número: ")
    numero2 = input("Digite o segundo número: ")
    numeros_validos = None
    try:
        #aqui eh feita a conv para float
        float_numero1 = float(numero1)
        float_numero2 = float(numero2)

        #se a conversao for feita com sucesso o parm muda para true
        numeros_validos = True
    except:
        #se a conversao for malsucedida o parm fica como None
        numeros_validos = None
    opcao = input("Qual a operação a ser realizada? \n1- soma(+) \n2- subtracao (-) \n3- 4multiplicacao (x)")

    #verificando se a opcao selecionado esta dentro das permitidas
    opcao_permitidas = '+-*xsomasubtracaomultiplicacao123'
    if opcao not in opcao_permitidas:
        print("Por favor selecione uma operacao valida!")
        continue

    #fazendo a validação se os numeros sao validos e informando:
    if numeros_validos is None:
        print("Os numeros nao sao validos... tente novamente.")
        continue # faz parar de ler e voltar ao inicio do laco while
    #validação das operacoes
    if opcao == 'soma' or opcao == "+":
        print('Soma dos fatores: ', float_numero1 + float_numero2)
    if opcao == 'subtracao' or opcao == "-":
        print('Subtracao dos fatores: ', float_numero1 - float_numero2)
    if opcao == 'multiplicacao' or opcao == "x":
        print('multiplicacao dos fatores: ', float_numero1 * float_numero2)

    sair = input('Voce quer sair s/n: ').lower().startswith('s') #lower para nao ter diferenca upper and lower
                                                 # e starts with para funcionar se for "sair", "sai" etc
    #faz a cond para sair do while e encerrar o programa
    if sair is True:
        break

    
    
    
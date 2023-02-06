#programa em python para adivinhar palavra secreta (parece jogo da forca)
#espaco por algum motivo funciona :/

palavra_secreta = "ELEFANTE" #estar sempre em maiuscula

numero_tentativas = 0

letras_acertadas = "" #salvo em uma variavel as letras que o usuario já acertou
print("A dica é que a palavra é um animal. Bom jogo!")
while True:
    palavra_atual = "" #coloco dentro do while para zerar a cada volta, senão repete

    letra_digitada = input("Digite uma letra: ").upper() #setando lera para uppercase

    if len(letra_digitada) > 1:
        print("voce digitou mais de um caracter, digite somente um por vez!")
        continue

    if letra_digitada not in palavra_secreta or letra_digitada == " ":
        numero_tentativas = numero_tentativas + 1
        continue

    if letra_digitada in palavra_secreta:
        #print(f"A letra {letra_digitada} esta na palavra secreta")
        letras_acertadas = letras_acertadas + letra_digitada
        #print("posicao letra", palavra_secreta.find(letra_digitada)) #aqui retorna a posicao da 1 letra encontrada
                                                                 #dentro da palavra secreta
        #print(f"Numero de tentativas: {numero_tentativas}")
        #continue

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_atual = palavra_atual + letra_secreta
        else:
            palavra_atual = palavra_atual + "*"
    print(palavra_atual)
    if palavra_atual == palavra_secreta:
        print("sua palavra esta completa")
        print(f"Numero de tentativas: {numero_tentativas}")
        break


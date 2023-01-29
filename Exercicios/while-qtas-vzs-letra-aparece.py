#programa em python para exibir quantas vezes a letra aparece numa frase.
#janeiro 19th - 2023

frase = 'Esse exercicio me ajudou a entender a logica por tras do whileiiiiiw'

i = 0
qtde_apareceu_mais_vezes = 0
qtde_apareceu_mais_vezes_atual = 0

letra_apareceu_mais_vezes_atual = "W"

while i < len(frase):
    letra_atual = frase[i]
    #atribui
    qtde_apareceu_mais_vezes = frase.count(letra_atual)
    #atribui
    print("letra atual: ", letra_atual)
    print("letra contador: ", qtde_apareceu_mais_vezes_atual)
    print("====" * 5)

    #salva a letra na var qtde_mais_vezes_atual se ela tiver repetido mais (tirando os espacos)
    if (qtde_apareceu_mais_vezes_atual < qtde_apareceu_mais_vezes and
    letra_atual not in " "):
        print("1 linha do if")
        qtde_apareceu_mais_vezes_atual = qtde_apareceu_mais_vezes
        print("3 linha do if")
        letra_apareceu_mais_vezes_atual = letra_atual
        print("Debug letra atual: ", letra_atual)
        print("Debug letra apareceu: ", letra_apareceu_mais_vezes_atual)
        
    i += 1

print(f"Letra que mais repetiu foi o {letra_apareceu_mais_vezes_atual}, que repetiu {qtde_apareceu_mais_vezes_atual} vezes.")

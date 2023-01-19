#iterando strings com while
#exerc preciso adicionar * a cada letra da minha string usando while

nome = 'Mariana Ferreira Lopes'

tamanho_nome = len(nome)
#print(nome)
#print(tamanho_nome)
#print(nome[3])

contador = 0
nova_string = ""
tamanho = len(nome)

while contador < tamanho:
    #print(nome[contador])
    nova_string = (nova_string + "*" + nome[contador])
    contador +=1
    

print("Nova string com asterisco: ", nova_string)
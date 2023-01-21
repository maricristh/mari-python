#usando o while para executar um bloco de codigo

condicao = True

count = 0

#primeiro while
while condicao: #enquanto for verdadeira o programa continua
    nome = input("Please insert a name: ")
    print(f"Seu nome eh {nome}")

    if nome == "sair": #quando o sair é informado o programa termina
        break

#segundo while
while count <10: #while is true execute this
   print(f"E contando.. {count}")
   count += 1

print("E acabou!!")

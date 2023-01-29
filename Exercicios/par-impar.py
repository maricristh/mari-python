#checar se é par ou impar ou se é um numero decimal

#numero = input("Please enter an integer number: ")

numero = input("Please enter an integer number: ")

#print (numero.isdecimal())
try:
    if (numero.isdigit() is False):
        print("O numero nao é inteiro, por favor tente novamente.")
    
    numero_int = int(numero) #faz a conversao para int

    if (numero_int % 2==0):
        print("O numero eh par!")
    else:
        print("O numero é impar!")
except:
    pass
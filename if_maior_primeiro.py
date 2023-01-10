#mostrar o valor maior primeiro

first_value = input('Digite um valor: ')
second_value = input('Digite um segundo valor: ')

print('e o resultado eh:')

if first_value > second_value:
    print("O ", first_value, " is greater than ", second_value)
elif second_value > first_value:
    print("Result ", second_value, " is greater than ", first_value)
else:
    print("Values ", first_value, " and ", second_value, " are similar")
    

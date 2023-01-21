print(1 + 1)

#usando o while

i =5
while i > 0:
	j = 0
	while j < 2:
		print(i, j)
		j = j + 1
	i -= 1

def imprimir_padrao():
    tamanho = 4
    for i in range(tamanho):
        print("*" * tamanho)
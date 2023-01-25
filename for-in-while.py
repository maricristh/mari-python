#programa para exibir letra a letra dentro de while e depois no FOR

texto = 'Mariane'
i = 0
tamanho_string = len(texto)
print("texto: ", texto)
print("i: ", i)
print("tamanho_string: ", tamanho_string)

while i < tamanho_string:
    print("texto", texto[i])
    i +=1

#programa usando o FOR:

print(f" Agora vamos usar o FOR", "===" * 5)

for letra in texto:
    print(f"dentro do FOR {letra}")

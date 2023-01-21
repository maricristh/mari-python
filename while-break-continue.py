#programa usando while, break e continue

contador = 0

while contador <=80:
    contador += 1
    
    if contador == 4:
        print("Nao vou mostrar o 4...")
        continue #continue faz a logica retornar ao while + proximo acima (pula a a cond da vez)

    print(f"Valor: {contador}")

    if contador == 25:
        break #para o laco do while


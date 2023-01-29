#programa python para mostrar tentativas incorretas de inserir a senha
senha = 'batata'
senha_digitada = ''
repeticoes = 0
print("Bem vindo ao nosso sistema, digite a senha para entrar")

while senha != senha_digitada:
    senha_digitada = input("digite sua senha: ")

    repeticoes +=1

print(f"Bem vindo ao sistema! Foram feitas {repeticoes-1} tentativas desde seu ultimo acesso")

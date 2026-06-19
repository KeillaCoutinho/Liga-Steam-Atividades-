print("Cadastro de Usuário")

nome = input("Digite seu nome completo: ")

while True:
    try:
        ano = int(input("Digite seu ano de nascimento: "))

        if ano < 1922 or ano > 2021:
            print("Ano inválido! Digite um valor entre 1922 e 2021.")
        else:
            break

    except:
        print("Erro! Digite apenas números.")

idade = 2022 - ano

print("\nNome:", nome)
print("Idade em 2022:", idade, "anos")
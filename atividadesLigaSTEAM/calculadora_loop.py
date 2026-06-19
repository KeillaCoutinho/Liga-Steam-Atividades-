while True:
    print("\n=== CALCULADORA ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Programa encerrado!")
        break

    elif opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro valor: "))
        num2 = float(input("Digite o segundo valor: "))

        if opcao == 1:
            resultado = num1 + num2
            print("Resultado:", resultado)

        elif opcao == 2:
            resultado = num1 - num2
            print("Resultado:", resultado)

        elif opcao == 3:
            resultado = num1 * num2
            print("Resultado:", resultado)

        elif opcao == 4:
            if num2 != 0:
                resultado = num1 / num2
                print("Resultado:", resultado)
            else:
                print("Não é possível dividir por zero!")

    else:
        print("Essa opção não existe!")
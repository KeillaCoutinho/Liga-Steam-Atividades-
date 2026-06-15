def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2
    elif operacao == 2:
        return num1 - num2
    elif operacao == 3:
        return num1 * num2
    elif operacao == 4:
        return num1 / num2
    else:
        return 0


# Testes
print(calculadora(10, 5, 1))  # Soma
print(calculadora(10, 5, 2))  # Subtração
print(calculadora(10, 5, 3))  # Multiplicação
print(calculadora(10, 5, 4))  # Divisão
print(calculadora(10, 5, 9))  # Operação inexistente
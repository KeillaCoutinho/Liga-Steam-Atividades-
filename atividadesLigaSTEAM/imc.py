def peso(peso, altura):
    imc = peso / (altura * 2 )
    if imc < 18.5:
        return "Abaixo do peso ideal"
    elif imc >= 18.5 and imc < 25:
        return "Peso ideal"
    else:
        return "Acima do peso ideal"

print(peso(50, 1.57))
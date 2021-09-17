"""def IMC(peso, altura):
    res = peso / (altura * altura)
    return round(res, 2)

peso = float(input("Dime el peso"))
altura = float(input("Dime la altura"))

print("Tu IMC es", IMC(peso, altura))"""

IMC_calculo = 0

peso = float(input("Dime el peso: "))
altura = float(input("Dime la altura: "))

IMC_calculo = peso / (altura * altura)
IMC_calculo = round(IMC_calculo, 2)

print("Tu IMC es", IMC_calculo)

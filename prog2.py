def IMC(peso, altura):
    res = peso / (altura * altura)
    return round(res, 2)

peso = float(input("Dime el peso"))
altura = float(input("Dime la altura"))

print("Tu IMC es", IMC(peso, altura))
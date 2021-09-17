n = int(input("Dime el numero de palabras: "))
listaPalabras = []

for i in range(n):
    print("-----------------")
    print("Palabra numero", i)
    palabra = str(input("Dime la palabra numero "))
    listaPalabras.append(palabra)


def main():
    print("Tu lista es:", listaPalabras)
"""Ejercicio 8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con
la letra a.
También se puede hacer elegir al usuario la letra a buscar. (Un poco mas
emocionante)"""

numero_nombres = int(input("Cuantos nombres quieres anyadir? "))
lista_nombres = []
numero_veces_letra = 0
letra_buscar = ""

if numero_nombres != 0:
    for palabras in range(numero_nombres):
        nombre = str(input("Dime el nombre: "))
        lista_nombres.append(nombre)

    letra_buscar = str(input("Que letra buscamos?: "))

    for palabra in lista_nombres:
        print(letra_buscar.lower(), "--", palabra[0].lower())
        if palabra[0].lower() == letra_buscar.lower():
            numero_veces_letra+=1
else:
    print("No puedo anyadir 0 nombres")

print("En la lista", lista_nombres, "hay", numero_veces_letra, "de la letra", letra_buscar)

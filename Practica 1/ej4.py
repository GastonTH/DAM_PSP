""" Ejercicio 4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa
tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene."""

def comprobar_mayusculas(cadena):
    numero_de_mayusculas = 0

    for i in cadena:
        if i != " " and i == i.upper():
            print(i.title())

cadena = str(input("Dime una cadena: "))
comprobar_mayusculas(cadena)
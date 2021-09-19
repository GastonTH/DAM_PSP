"""Ejercicio 7
Definir una tupla con 10 edades de personas. Imprimir la cantidad de personas con
edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""
def crear_tupla(numero):
    
    tupla_return = []
    for anyadir in range(numero):
        tupla_return.append(int(input("Dime una edad: ")))

    return(tuple(tupla_return))

#tupla_personas_edades = (15,15,20,98,2,64,34,21,99,100,129,65)
mayor_de_n = 0
numero = int(input("Cuantas edades quieres anyadir: "))

if numero != 0:
    tupla_personas_edades = crear_tupla(numero)

    for edad in tupla_personas_edades:
        if edad >= 20:
            mayor_de_n+=1

    print("hay mayores de 20", mayor_de_n, "personas")
"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla"""

from datetime import datetime
from dateutil.relativedelta import relativedelta

def crear_diccionario_de_fechas(numero_de_fechas):

    personas_fechas = {}

    for i in range(numero_de_fechas):
        nombre = input("Dime el nombre de la persona: ")
        fecha = input("Dime su fecha de nacimiento: (DD/MM/YYYY): ")
        personas_fechas[nombre] = fecha
        print(10*"-", "\n")
    return personas_fechas

def preguntar_edad_cumplida(diccionario):

    hoy = datetime.now()

    for key, value in diccionario.items():
        fecha = datetime.strptime(value, "%d/%m/%Y")
        edad = relativedelta(hoy, fecha)

        if (hoy.day >= fecha.day and hoy.month >= fecha.month):
            print("-- > ya ha cumplido los años")
        else:
            print("-- >aun no los ha cumplido")

        print(key, "tiene", edad.years, "años")

numero_personas = int(input("Cuantas personas quieres anyadir: "))

if(numero_personas != 0):
    diccionario_personas = dict(crear_diccionario_de_fechas(numero_personas))
    preguntar_edad_cumplida(diccionario_personas)
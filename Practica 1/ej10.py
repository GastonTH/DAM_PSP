"""Ejercicio 10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por
400"""
"""
anyo = int(input("Dime el anyo"))

if anyo % 4 != 0:
	print("No es bisiesto")
    
elif anyo % 4 == 0 and anyo % 100 != 0:
	print("Es bisiesto")

elif anyo % 4 == 0 and anyo % 100 == 0 and anyo % 400 != 0: 
	print("No es bisiesto")

elif anyo % 4 == 0 and anyo % 100 == 0 and anyo % 400 == 0:
	print("Es bisiesto")"""

from calendar import isleap

anyo = int(input("Dime el anyo: "))

if isleap(anyo):
    print("es bisiesto")
else:
    print("no es bisiesto")
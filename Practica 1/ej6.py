"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla"""

import datetime

#anyo_curso = input("Dime el anyo del curso")

hoy = datetime.datetime.today()
print("hoy", hoy)

lista_persona_anyo = {
    'Alumno1' : 'Pepe', 'Fecha1' : datetime.datetime(1999,2,6),
    'Alumno2' : 'Carlos', 'Fecha2' : datetime.datetime(1999,11,1),
    'Alumno3' : 'Juan', 'Fecha3' : datetime.datetime(1993,7,29),
}

for persona, fecha in lista_persona_anyo.items():

    print(persona, "-", fecha)
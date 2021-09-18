"""Ejercicio 6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla"""

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

anyo_curso = 2021

hoy = datetime.now()
fin_curso = datetime(anyo_curso, 6, 22)
#print("Hoy:", hoy, "\nFinal de curso", fin_curso)

lista_persona_anyo = {
    'Alumno1' : 'Pepe', 'Fecha1' : datetime(1999,2,6),
    'Alumno2' : 'Carlos', 'Fecha2' : datetime(1999,11,1),
    'Alumno3' : 'Juan', 'Fecha3' : datetime(1993,7,29),
}

"""print(hoy)

for persona, fecha in lista_persona_anyo.items():

    print(persona, "-", fecha)
"""

"""ahora = datetime.now()
hace_una_semana = ahora - timedelta(year=7)
print(hace_una_semana)"""

for persona, fecha in lista_persona_anyo.items():
    print(persona,"- - -", fecha)

"""relativedelta <---<----<<-<<-<<--<<<-<<--<<-----------------------------------"""
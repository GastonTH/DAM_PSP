"""Ejercicio 9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras
"a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra."""

def contar_vocales(palabra):

    veces_a = palabra.lower().count("a")
    veces_e = palabra.lower().count("e")
    veces_i = palabra.lower().count("i")
    veces_o = palabra.lower().count("o")
    veces_u = palabra.lower().count("u")

    return veces_a, veces_e, veces_i, veces_o, veces_u

palabra_input = str(input("Dime una palabra: "))

a,e,i,o,u = contar_vocales(palabra_input)

print("Veces a =", a, ", veces e =", e, ", veces i =", i, ", veces o =", o, "y veces u =", u)
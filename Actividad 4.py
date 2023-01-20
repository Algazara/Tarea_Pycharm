"""Escribir un programa que almacene la cadena de caracteres 12345EDD como contraseña.
En una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta"""

def actividad4():
    clave=input("Indica tu contraseña")
    while clave!="12345EDD":
        clave = input("Indica tu contraseña")

    return clave

actividad4()

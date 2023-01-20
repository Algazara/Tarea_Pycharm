"""Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
y muestre por pantalla el menor y el mayor de los precios"""

def actividad7():
    lista_precios=[50, 75, 46, 22, 80, 65, 8]
    precio_mayor=0
    precio_menor=0

    for i in lista_precios:
        if i<precio_menor:
            precio_menor=i
        if i>precio_mayor:
            precio_mayor=i

    print(precio_menor, precio_mayor)
actividad7()

#La función debug muestra que la variable precio_menor tiene siempre valor 0, por lo que la condición nunca se cumple
#Para que la condición se cumpla, debe tener un valor de los que se encuentran en la lista para compararlo. Por tanto,
#la variable se inicia con el valor de la posición 0 de la lista y el resto de números se comparan con respecto a este
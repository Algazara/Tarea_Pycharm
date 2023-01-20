"""El programa debe almacenar los vectores (1, 2, 3) y (-1, 0, 2)
en dos listas y muestre por pantalla su producto escalar"""

def actividad2():
    a=(1,2,3)
    b=(-1,0,2)
    product=0
    for i in range (len(a)+1):
        product=a[i-1]*b[i-1]
    print("El producto de los vectores " + str(a) + " y" + str(b) + " es" + str(product))

actividad2()

#Se muestra un error en la línea del bucle for indicando que solo es posible concatenar una tupla con otra tupla, no con un entero.
# Al eliminar el +1 de len(a), se resuelve el problema
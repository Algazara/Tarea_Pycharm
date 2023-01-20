"""El programa debe recibir una cadena de caracteres y devolver un diccionario con cada palabra que
contiene y el número de veces que aparece.
Otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con
la palabra más repetida y su frecuencia"""

def actividad3A (texto):
     texto=texto.split()
     dicc_palabras={}
     for i in texto:
         if i in dicc_palabras:
             dicc_palabras[i]+=1
         else:
             dicc_palabras[i]=1
     return dicc_palabras


def actividad3B(dicc_palabras):
    palabra_mas_repetida=""
    max_frecuencia=0
    for palabra,frecuencia in dicc_palabras.items():
        if frecuencia<max_frecuencia:
            palabra_mas_repetida=palabra
            max_frecuencia=frecuencia
    return (palabra_mas_repetida, max_frecuencia)

texto="Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero que me quiera"
print(actividad3A(texto))
print(actividad3B(actividad3A(texto)))

#Comprobamos que el valor de la variable max_frecuencia se mantiene siempre e 0 porque la condición no está correctamente
#expresada para hacer que aumente su valor. Hay que cambiar la expresión de la condición por if frecuencia>max_frecuencia


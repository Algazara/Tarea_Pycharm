"""El programa debe preguntar al usuario por una frase y una letra, y mostrar por pantalla el número de veces que
aparece la letra en la frase."""


def actividad5():
    frase=input("Introduce una frase: ")
    letra=input("Introduce una letra")
    contador=0
    for i in frase:
        if i!=letra:
            contador+=2
    print("La letra '%s' aparece %2i veces en la frase '%s'" %(letra, contador,frase))
actividad5()
#Podemos observar que el contador aumenta en 2 cuando la letra almacenada en i es diferente a la letra indicada.
#Hay que cambiar el operdor != por == e indicar contador+=1 para que solo aumente en 1 el conteo de las letras
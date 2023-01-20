"""Escribe un programa que almacene las asignaturas de un curso (por ejemplo Informática, Francés, Filosofía, Ética y Álgebra) en una lista y la muestre por pantalla el mensaje “Yo estudio <asignatura>”, donde “asignatura” es cada una de las asignaturas de la lista.
Una vez terminado, documenta con el historial de VCS los diferentes estados por los que ha pasado tu código."""

def actividad1 ():
    lista_asignaturas=["Informática", "Francés", "Filosofía", "Ética", "Álgebra"]
    for i in range(len(lista_asignaturas)):
        asignatura=lista_asignaturas[i]
        print("Yo estudio", asignatura)

actividad1()


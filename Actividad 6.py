"""El programa debe almacenar las matrices en una lista y mostrar por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista"""

a=((1,2,3))
b=((-1, 0), (0,1), (1,1))

result=[[0,0], [0,0]]

def actividad6():

    for i in range (len(a)):
        for j in range (len([b])):
            for k in range (len(b)):
                result[i][j]+=a[j][j]*b[j][i]
    for i in range (len(result)):
        result[i]=tuple(result[i])
    result=tuple(result)

    for i in range (len(result)):
        print(result[i])

actividad6()





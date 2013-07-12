# Funcion que toma una lista de numeros y quita todos los impares

def purificar(lista):
    print lista
    i=0
    while i in range(0, len(lista)):
        if lista[i] %2 != 0:
            del lista[i]
        else:
            i+=1
        print lista
    return lista
print purificar([1,2,3])

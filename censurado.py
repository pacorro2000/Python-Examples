def censor(texto, palabra):
    p= len(palabra)
    t= len(texto)

    asteriscos=""
    for c in palabra:
        asteriscos+= "*"

    textoCensurado=""
    i=0
    while (i<t):
        if texto[i:i+p]==palabra:
            textoCensurado+=asteriscos
            i=i+p
        else:
            textoCensurado+=texto[i]
            i+=1

    return textoCensurado

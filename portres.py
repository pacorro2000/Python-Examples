#!/usr/bin/env python

""" Escribir una funcion, por_tres, que llame a una segunda funcion,
cubo, si un numero es divisible por 3 u que sea False en caso contrario.
Luego debes retornar el resutlado que te de la funcion cubo.
En cuanto a la funcion cubo, esta debe retornar el numero que le pasa la
funcion por_tres elevado al cubo.
Por ultimo, llama a por_tres con los numero 11, 12 y 13 en tres lineas 
diferentes. """

def por_tres(n):
    if n % 3 == 0:
        return cubo(n)
    else:
        return False

def cubo(n):
    return n**3


por_tres(11)
por_tres(12)
por_tres(13)

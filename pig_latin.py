#! /usr/bin/env python

""" Este es un programa que convierte una palabra en 
espanol a pig latin """

print "!Bienvenido al traductor de Espanol a Pig Latin!"

pyg = 'ei' # Se agrega a la traduccion de pig latin

""" Pedimos al usuario introducir una palabra que sera almacenada en la variable original """
original = raw_input("Ingresa la palabra a traducir: ")

""" Verficando que la cadena no este vacia y que contenga caracteres alfanumericos, 
ademas de que verificamos si comienza con vocal o consonante """

if len(original) >= 0 and original.isalpha(): 
    palabra = original.lower() # Convirtiendo a minusculas
    primera = palabra[0] # Obteniendo el primer caracter
    
    if primera == 'a' or primera == 'e' or primera == 'i' or primera == 'o' or primera == 'u': # Si es vocal
        nueva_palabra = palabra + pyg
        print nueva_palabra
    else:
        nueva_palabra = palabra[1:] + palabra[0] + pyg # Si es consonate se elimina y se pone al final con 'ei'
        print nueva_palabra

else:
    print "Vacio o no valido"


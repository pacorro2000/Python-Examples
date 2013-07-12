#!/usr/bin/env python

# Funcion que limpia pantalla dependiendo de el OS
import os

def clear():
	if os.name == "posix":
		os.system("clear")
	elif os.name == ("ce", "nt", "dos"):
		os.system("cls")
		
clear()

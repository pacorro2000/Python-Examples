#!/usr/bin/env python

import math

def es_entero(x):
    x = abs(x)
    x2 = math.floor(x)

    if (x2 - x) >= 0:
        return True
    else:
        return False

print es_entero(-3.2)

#!/usr/bin/env python

def factorial(x):
    s = 1
    while x > 0:
        s *= x
        x -= 1
    return s

print factorial(5)

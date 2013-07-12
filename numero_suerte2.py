from random import randrange

numero_aleatorio = randrange(1, 10)

count = 0
# arranca tu juego!
while count < 3:
    adivina = int(raw_input("Adivina un numero: "))
    print adivina
    count += 1
    if adivina == numero_aleatorio:
        print "Tu ganas!"
        break
else:
    print "Tu pierdes"

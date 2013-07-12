from random import randint

print "¡Números de la suerte! Se generarán 3 números."
print "Si uno de ellos es '5', ¡pierdes!"

recuento = 0
while recuento < 3:
	num = randint(1, 6)
	print num
	recuento += 1
	if num == 5:
		print "Lo lamento, ¡tú pierdes!"
		break
else:
	print "¡Tú ganas!"

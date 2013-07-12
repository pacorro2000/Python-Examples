frutas = ['banana', 'manzana', 'naranja', 'tomate', 'pera', 'uva']

print 'Tienes...'
for f in frutas:
    if f == 'tomate':
        print 'El tomate no es una fruta'
        break
    print f
else:
    print 'Una seleccion exclusiva de frutas'

'''cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))
hipot = ((cat_op ** 2) + (cat_ad ** 2)) ** (1/2)
print('Em um triangulo que o cateto oposto seja {} e o adjadente seja {} a hipotenusa é {:.2f}'.format(cat_op, cat_ad, hipot))'''

from math import hypot
cat_op = float(input('Comprimento do cateto oposto: '))
cat_ad = float(input('Comprimento do cateto adjacente: '))
hipot = hypot(cat_op, cat_ad)
print('Em um triangulo que o cateto oposto seja {} e o adjadente seja {} a hipotenusa é {:.2f}'.format(cat_op, cat_ad, hipot))


real = float(input('Quanto dinhero você tem na carteira? R$'))
realdolar = float(input('Qual o valor do dolar hoje? U$'))
dolar = real / realdolar
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))

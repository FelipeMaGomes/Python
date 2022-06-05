distância = float(input('Qual é distãncia de sua viagem? '))
print('Voçê está prestes a começar uam viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço de sua passagem será de R${:.2f}'.format(preço))
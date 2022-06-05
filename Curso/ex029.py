velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >80:
    print('\033[31mMULTADO! Voçê excedeu o limite permitido que é de 80Km/h\033[m')
    multa = (velocidade-80) * 7
    print('\033[31mVoçê deve pagar uma multa de R${:.2f}!\033[m'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')

print('{:=^40}'.format('\033[;36m LOJAS GUANABARA \033[m'))
preço = float(input('\033[;33mPreço das compras: R$\033[m'))
print('''\033[;32mFORMAS DE PAGAMENTO
[ 1 ] á vista dinheiro/cheque
[ 2 ] á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m''')
opção = int(input('\033[;35m Qual é a opção? \033[m'))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('\033[;33mSua compra será parcelada em 2x de R${:.2f}\033[;31m SEM JUROS\033[m'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('\033[;34mQuantoas parcelas?\033[m'))
    parcela = total / totparc
    print('\033[;33mSua compra será parcelada em {}x R${:.2f}\033[;36m COM JUROS\033[m'.format(totparc, parcela))
else:
    total = 0
    print('\033[;31mOPÇÃO INVÁLIDA de pagamento. Tente novamente!\033[m')
print('\033[;32mSua compra de R${:.2f} vai cusatar R${:.2f} no final.\033[m'.format(preço, total))
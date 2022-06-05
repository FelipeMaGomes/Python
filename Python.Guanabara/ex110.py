from teste import moeda


def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')

def resumo(preço=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado \t{moeda(preço)}')
    print(f'Dobro do preço: \t{dobro(preço)}')
    print(f'Metade do preço: \t{metade(preço)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preço, taxaa)}')
    print(f'{taxar}% de redução: \t{diminuir(preço, taxar)}')
    print('-' * 30)

p = float(input('Digite o preço: R$'))
resumo(p, 20, 12)

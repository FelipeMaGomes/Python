def aumentar(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def drobro(preço):
    res = preço * 2
    return res

def metade(preço):
    res = preço / 2
    return res


p = float(input('Digite o preço: R$'))
print(f'A metade de R${p} é R${metade(p)}')
print(f'O drobo de R${p} é R${drobro(p)}')
print(f'Aumentado 10%, temos R${aumentar(p, 10)}')

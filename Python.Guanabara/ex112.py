def LeiaDinheiro(msg):
    válido = False
    while not válido:
        entrada  = str(input(msg))
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço invalido!\033[m')
        else:
            válido = True
            return float(entrada)

def aumentar(preço = 0, taxa = 0):
    res = preço + (preço * taxa/100)
    return res


def diminuir(preço = 0, taxa = 0):
    res = preço - (preço * taxa/100)
    return res


def drobro(preço = 0):
    res = preço * 2
    return res

def metade(preço = 0):
    res = preço / 2
    return res

def moeda(preço = 0):
    res = preço / 2
    return res

def moeda(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


p = LeiaDinheiro('Digite o preço: R$')
print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O drobo de {moeda(p)} é {moeda(drobro(p))}')
print(f'Aumentado 10%, temos R${moeda(aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda(diminuir(p, 13))}')
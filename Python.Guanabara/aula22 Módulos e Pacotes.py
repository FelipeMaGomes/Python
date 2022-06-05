def fatorial(n):
    resp = 'snSN'
    f = 1
    for c in range(1, n+1):
        f *= c
    return f


while True:
    num = int(input('Digite um valor: '))
    fat = fatorial(num)
    print(f'O fatorial de {num} é {fat}.')
    resp = str(input('Quer continuar? [S/N] '))
    if resp == 'n':
        break
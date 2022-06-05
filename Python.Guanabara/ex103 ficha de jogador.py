print('----------------------------------------')
print('         CAMPEONATO DE FUTEBOL          ')
print('----------------------------------------')
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gols(s) no campeonato.')


# PRINCIPAL
n = str(input("Nome do Jogador: "))
g = str(input("Número de Gol: "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

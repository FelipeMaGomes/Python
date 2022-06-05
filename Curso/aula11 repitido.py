nome = 'Guanabara'
cores = {'Limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'preto e branco':'\033[7;30m'}

print('Olá! Muito prazer em te conhcer {}{}{}!!'.format(cores['preto e branco'], nome, cores['Limpa']))
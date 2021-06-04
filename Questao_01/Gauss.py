matriz = [3, 2, 0, 1, 3, 9, 8, -3, 4, 6, -6, 4, -8, 0, -16, 3, -8, 3, -8, 22]

# Linha 1 = matriz[0:5]
# Linha 2 = matriz[5:10]
# Linha 3 = matriz[10:15]
# Linha 4 = matriz[15:20]
# pivô = 3
# mL2 = 9/3 = 3
# mL3 = -6/3 = -2
# mL4 = 3/3 = 1
# Nova linha 2 = L2 - mL2 * L1
# Nova linha 3 = L3 - mL3 * L1
# Nova linha 4 = L4 - ml4 * L1

matriz_1a_iteracao = [3, 2, 0, 1, 3]

# Fazendo a nova linha 2 (1):
for c in range(5, 10):
    elemento_1 = matriz[c] - (3 * matriz[c-5])
    matriz_1a_iteracao.append(elemento_1)

# Fazendo a nova linha 3 (1):
for c in range(10, 15):
    elemento_1 = matriz[c] - (-2 * matriz[c - 10])
    matriz_1a_iteracao.append(elemento_1)

# Fazendo a nova linha 4 (1):
for c in range(15,20):
    elemento_1 = matriz[c] - (1 * matriz[c - 15])
    matriz_1a_iteracao.append(elemento_1)

matriz_2a_iteracao = [3, 2, 0, 1, 3, 0, 2, -3, 1, -3]
# Novo pivô = 2
# Novo mL3 = 8/2 = 4
# Novo ml4 = -10/2 = -5

# Fazendo a nova linha 3 (2):
for c in range(10, 15):
    elemento_2 = matriz_1a_iteracao[c] - (4 * matriz_1a_iteracao[c-5])
    matriz_2a_iteracao.append(elemento_2)

# Fazendo a nova linha 4 (2):
for c in range(15, 20):
    elemento_2 = matriz_1a_iteracao[c] - ((-5) * matriz_1a_iteracao[c-10])
    matriz_2a_iteracao.append(elemento_2)

# Novo pivô = 4
# Novo mL4 = -12 / 4 = -3

matriz_3a_iteracao = [3, 2, 0, 1, 3, 0, 2, -3, 1, -3, 0, 0, 4, -2, 2]

# Fazendo a nova linha 4 (3):
for c in range(15, 20):
    elemento_3 = matriz_2a_iteracao[c] - ((-3) * matriz_2a_iteracao[c-5])
    matriz_3a_iteracao.append(elemento_3)

# Matriz triangular superior = matriz_3a_iteracao.

print('Teremos a seguinte matriz aumentada equivalente: ')
print(f'[{matriz_3a_iteracao[0:5]}, '
      f'{matriz_3a_iteracao[5:10]},'
      f'{matriz_3a_iteracao[10:15]},'
      f'{matriz_3a_iteracao[15:20]}]')

# Resolvendo a matriz triangular superior

# Transformando em formato de matriz:
U = [[3, 2, 0, 1], [0, 2, -3, 1], [0, 0, 4, -2], [0, 0, 0, -10]]  # Icógnitas
b = [3, -3, 2, 10]  # Valores independentes


def resultado_matriz_triangular(U, b):
    n = len(b)
    x = [0]*n
    x[n-1] = b[n-1]/U[n-1][n-1]

    for i in list(range(n-1, 0, -1)):
        s = 0
        for j in list(range(i+1, n+1, 1)):
            s = s + U[i-1][j-1]*x[j-1]
        x[i-1] = (b[i-1] - s)/(U[i-1][i-1])

    return x


valores_x = resultado_matriz_triangular(U, b)
print('Os valores finais de x serão: ')
for c, v in enumerate(valores_x):
    print(f'X{c + 1} = {v}')

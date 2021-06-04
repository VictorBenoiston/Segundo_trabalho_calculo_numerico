# matriz = [3, 2, 0, 1, 3, 9, 8, -3, 4, 6, -6, 4, -8, 0, -16, 3, -8, 3, -8, 22]
# Como na fatoração Lu não será utilizada a matriz dos valores independentes (b), temos apenas:
matriz = [[3, 2, 0, 1], [9, 8, -3, 4], [-6, 4, -8, 0], [3, -8, 3, -8]]

# Repetindo os passos, porém com a matriz A:
# pivô = 3
# mL2 = 3
# mL3 = -2
# mL4 = 1

matriz_1a_iteracao = matriz[0]

# Fazendo a nova linha 2 (1):
for c in range(0, 4):
    elemento_1 = matriz[1][c] - (3 * matriz[0][c])
    matriz_1a_iteracao.append(elemento_1)

# Fazendo a nova linha 3 (1):
for c in range(0, 4):
    elemento_1 = matriz[2][c] - ((-2) * matriz[0][c])
    matriz_1a_iteracao.append(elemento_1)

# Fazendo a nova linha 4 (1):
for c in range(0, 4):
    elemento_1 = matriz[3][c] - (1 * matriz[0][c])
    matriz_1a_iteracao.append(elemento_1)

matriz_2a_iteracao = [3, 2, 0, 1, 0, 2, -3, 1]
# Novo pivô = 2
# Novo ml3 = 4
# Novo ml4 = -5

# Fazendo a nova linha 3 (2):
for c in range(8, 12):
    elemento_2 = matriz_1a_iteracao[c] - (4 * matriz_2a_iteracao[c-4])
    matriz_2a_iteracao.append(elemento_2)

# Fazendo a nova linha 4 (2):
for c in range(12, 16):
    elemento_2 = matriz_1a_iteracao[c] - ((-5) * matriz_2a_iteracao[c-8])
    matriz_2a_iteracao.append(elemento_2)

# Novo pivô = 4
# Novo mL4 = -3

matriz_3a_iteracao = [3, 2, 0, 1, 3, 0, 2, -3, 1, -3, 0, 0, 4, -2, 2]

# Fazendo a nova linha 4(3):
for c in range(12, 16):
    elemento_3 = matriz_2a_iteracao[c] - ((-3) * matriz_2a_iteracao[c-4])
    matriz_3a_iteracao.append(elemento_3)

# A matriz L é formada da matriz triangular, e dos elementos multiplicadores, temos:
L = [[1, 0, 0, 0], [3, 1, 0, 0], [-2, 4, 1, 0], [1, -5, -3, 1]]

# A matriz u é igual a matriz resultante do escalonamento>
u = [[3, 2, 0, 1], [0, 2, -3, 1], [0, 0, 4, -2], [0, 0, 0, -10]]
b = [3, 6, -16, 22]

# Achando y:


def resultado_matriz_triangular_inferior(L, b):
    n = len(b)
    y = [0]*n

    for i in list(range(1, n + 1, 1)):
        s = 0
        for j in list(range(1, i, 1)):
            s = s + L[i-1][j-1]*y[j-1]
        y[i-1] = b[i-1] - s

    return y

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


print(f'A matriz L é dada por: {L}')
print(f'A matriz u é dada por: {u}')
print(f'O resultado de y é: ')
y = resultado_matriz_triangular_inferior(L, b)
print(y)

print(f'Portanto, o resultado final é: ')
teste2 = resultado_matriz_triangular(u, y)
for c, v in enumerate(teste2):
    print(f'X{c} = {v}')

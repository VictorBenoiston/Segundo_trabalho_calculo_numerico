matriz = [[3, 2, 0, 1], [9, 8, -3, 4], [-6, 4, -8, 0], [3, -8, 3, -8]]
b = [3, 6, -16, 22]
x0 = [1, (2/3), (8/3), (22/3)]


def valores_de_x_atualizados(list, b, x_atual):
    lista_valores_atualizados = []
    x1 = (1/list[0][0])*(b[0]-(list[0][1] * x_atual[1]) - (list[0][2] * x_atual[2]) - (list[0][3] * x_atual[3]))
    x2 = (1/list[1][1])*(b[1]-(list[1][0] * x1) - (list[1][2] * x_atual[2]) - (list[1][3] * x_atual[3]))
    x3 = (1/list[2][2])*(b[2]-(list[2][0] * x1) - (list[2][1] * x2) - (list[2][3] * x_atual[3]))
    x4 = (1/list[3][3])*(b[3]-(list[3][0] * x1) - (list[3][1] * x2) - (list[3][2] * x3))
    lista_valores_atualizados = [x1, x2, x3, x4]
    return lista_valores_atualizados


def modulo(list):
    modulo_list = []
    for item in list:
        if item < 0:
            modulo_item = item * (-1)
            modulo_list.append(modulo_item)
        else:
            modulo_item = item
            modulo_list.append(modulo_item)
    return modulo_list


# Primeira iteração:
x1 = valores_de_x_atualizados(matriz, b, x0)
modulo_x0 = modulo(x0)
modulo_x1 = modulo(x1)

# Critério de parada (0):
dr = [(modulo_x1[0]-modulo_x0[0]), (modulo_x1[1]-modulo_x0[1]), (modulo_x1[2]-modulo_x0[2]), (modulo_x1[3]-modulo_x0[3])]
modulo_dr = modulo(dr)
resultado = max(modulo_dr)/max(modulo_x1)
print('O valor de dr da primeira iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')

# Segunda iteração:
x2 = valores_de_x_atualizados(matriz, b, x1)
modulo_x2 = modulo(x2)

# Critério de parada (1):
dr1 = [(modulo_x2[0]-modulo_x1[0]), (modulo_x2[1]-modulo_x1[1]), (modulo_x2[2]-modulo_x1[2]), (modulo_x2[3]-modulo_x1[3])]
modulo_dr1 = modulo(dr1)
resultado = max(modulo_dr1)/max(modulo_x2)
print('O valor de dr da segunda iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')

# Terceira iteração:
x3 = valores_de_x_atualizados(matriz, b, x2)
modulo_x3 = modulo(x3)

# Critério de parada (2):
dr2 = [(modulo_x3[0]-modulo_x2[0]), (modulo_x3[1]-modulo_x2[1]), (modulo_x3[2]-modulo_x2[2]), (modulo_x3[3]-modulo_x2[3])]
modulo_dr2 = modulo(dr2)
resultado = max(modulo_dr2)/max(modulo_x3)
print('O valor de dr da  terceira iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')

# Quarta iteração:
x4 = valores_de_x_atualizados(matriz, b, x3)
modulo_x4 = modulo(x4)

# Critério de parada (3):
dr3 = [(modulo_x4[0]-modulo_x3[0]), (modulo_x4[1]-modulo_x3[1]), (modulo_x4[2]-modulo_x3[2]), (modulo_x4[3]-modulo_x3[3])]
modulo_dr3 = modulo(dr3)
resultado = max(modulo_dr3)/max(modulo_x4)
print('O valor de dr da  quarta iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')

# Quinta iteração:
x5 = valores_de_x_atualizados(matriz, b, x4)
modulo_x5 = modulo(x5)

# Critério de parada (4):
dr4 = [(modulo_x5[0]-modulo_x4[0]), (modulo_x5[1]-modulo_x4[1]), (modulo_x5[2]-modulo_x4[2]), (modulo_x5[3]-modulo_x4[3])]
modulo_dr4 = modulo(dr4)
resultado = max(modulo_dr4)/max(modulo_x5)
print('O valor de dr da  quinta iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')

# Sexta iteração:
x6 = valores_de_x_atualizados(matriz, b, x5)
modulo_x6 = modulo(x6)

# Critério de parada (5):
dr5 = [(modulo_x6[0]-modulo_x5[0]), (modulo_x6[1]-modulo_x5[1]), (modulo_x6[2]-modulo_x5[2]), (modulo_x6[3]-modulo_x5[3])]
modulo_dr5 = modulo(dr5)
resultado = max(modulo_dr5)/max(modulo_x6)
print('O valor de dr da  sexta iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')
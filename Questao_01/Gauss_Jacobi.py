matriz = [[3, 2, 0, 1], [9, 8, -3, 4], [-6, 4, -8, 0], [3, -8, 3, -8]]
# e = 10^-5
# Xo = bi/aii

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

# Encontrando o Xo:
x0 = [1, (2/3), (8/3), (22/3)]
modulo_x0 = modulo(x0)

# Resolvendo a primeira iteração:
x1 = [((1/3) * (3-(2 * (2/3))-(22/3))), ((1/8) * (6 - 9 - (-3 * (8/3)) - (4 * (22/3)))), ((1/-8) * (-16 - (-6) - (4 * (2/3)))), ((1/-8) * (22 - 3 - (-8 * (2/3)) - (3 * (8/3))))]

modulo_x1 = modulo(x1)

# Critério de parada (0):
dr = [(modulo_x1[0]-modulo_x0[0]), (modulo_x1[1]-modulo_x0[1]), (modulo_x1[2]-modulo_x0[2]), (modulo_x1[3]-modulo_x0[3])]
modulo_dr = modulo(dr)
resultado = max(modulo_dr)/max(modulo_x1)
print(f'x1 = {x1}')
print('O valor de dr da primeira iteração, foi de: ')
print(resultado)
print('Ainda não é menor que 10^-5')
print('----------------------------------')

#Resolvendo a segudna iteração:
x2 = [((1/3) * (3-(2 * (x1[1]))-(x1[3]))), ((1/8) * (6 - (9*x1[0]) - (-3 * (x1[2])) - (4 * (x1[3])))), ((1/-8) * (-16 - (-6 * x1[0]) - (4 * (x1[1])))), ((1/-8) * (22 - (3 * x1[0]) - (-8 * (x1[1])) - (3 * (x1[2]))))]

modulo_x2 = modulo(x2)

# Critério de parada (1):
dr1 = [(modulo_x2[0]-modulo_x1[0]), (modulo_x2[1]-modulo_x1[1]), (modulo_x2[2]-modulo_x1[2]), (modulo_x2[3]-modulo_x1[3])]
modulo_dr1 = modulo(dr1)

resultado1 = max(modulo_dr1)/max(modulo_x2)
print(f'x2 = {x2}')
print('O critério de parada dr da segunda iteração, foi de: ')
print(resultado1)
print('Ainda não é menor que 10^-5')
print('----------------------------------')


# Resolvendo a terceira iteração:
x3 = [((1/3) * (3-(2 * (x2[1]))-(x2[3]))), ((1/8) * (6 - (9*x2[0]) - (-3 * (x2[2])) - (4 * (x2[3])))), ((1/-8) * (-16 - (-6 * x2[0]) - (4 * (x2[1])))), ((1/-8) * (22 - (3 * x2[0]) - (-8 * (x2[1])) - (3 * (x2[2]))))]

modulo_x3 = modulo(x3)

# Citério de parada (2):
dr2 = [(modulo_x3[0]-modulo_x2[0]), (modulo_x3[1]-modulo_x2[1]), (modulo_x3[2]-modulo_x2[2]), (modulo_x3[3]-modulo_x2[3])]
modulo_dr2 = modulo(dr2)

resultado2 = max(modulo_dr2)/max(modulo_x3)
print(f'x3 = {x3}')
print('O critério de parada dr da terceira iteração, foi de: ')
print(resultado2)
print('Ainda não é menor que 10^-5')

x = [0, 6, 10]
y = [6.67, 17.33, 42.67]

# p2_x = L0*f(x0) + L1 * f(x1) + L2 * f(x2)


def lx(x, valores_x):
    l0 = ((x - valores_x[1]) * (x - valores_x[2])) / ((valores_x[0] - valores_x[1]) * (valores_x[0] - valores_x[2]))
    l1 = ((x - valores_x[0]) * (x - valores_x[2])) / ((valores_x[1] - valores_x[0]) * (valores_x[1] - valores_x[2]))
    l2 = ((x - valores_x[0]) * (x - valores_x[1])) / ((valores_x[2] - valores_x[0]) * (valores_x[2] - valores_x[1]))
    return l0, l1, l2


def p2(y, l0, l1, l2):
    resultado = (y[0] * l0) + (y[1] * l1) + (y[2] * l2)
    return resultado


# Como queremos saber o que acontece no dia 7, temos:
l0 = lx(7, x)[0]
l1 = lx(7, x)[1]
l2 = lx(7, x)[2]

px_7 = p2(y, l0, l1, l2)


print(f'Por meio do método de Lagrange, temos: ')
print(f'No dia 07, a amostra atinge: {px_7:.2f}g')

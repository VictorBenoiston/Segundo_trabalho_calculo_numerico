x = [0, 6, 10]
y = [6.67, 17.33, 42.67]

# Esse será o polinomio de segundo grau.
def d_2_grau(x, y):
    d0 = [y[0], y[1], y[2]]
    d1 = [((d0[1] - d0[0])/ (x[1] - x[0])), ((d0[2] - d0[1])/(x[2] - x[1]))]
    d2 = (d1[1]-d1[0])/(x[2] - x[0])
    return d0, d1, d2

d0 = d_2_grau(x, y)[0]
d1 = d_2_grau(x, y)[1]
d2 = d_2_grau(x, y)[2]

def p2(x,valores_x, d0, d1, d2):
    resultado = d0[0] + (d1[0] * (x - valores_x[0])) + (d2 * ((x - valores_x[0]) * (x - valores_x[1])))
    return resultado

valor_aplicado = p2(7, x, d0, d1, d2)

print(f'Por meio do método de Newton, temos: ')
print(f'No dia 07, a amostra atinge: {valor_aplicado:.2f}g')

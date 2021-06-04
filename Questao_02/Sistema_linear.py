from math import sqrt
# Montando o sistema em si, é possível notarmos que c = 6,67
# Daí, ficamos com:
# Linha 1: 36a+6b+c=17.33
# Linha 2: 100a+10b+c=42.67

# Achando a e b por meio de escalonamento:
matriz = [[36, 6, 10.66], [100, 10, 36]]

# Pivô = 36
# mL2 = 100/36 = 25/9
# Achando a nova linha 2:
x = [36, 6, 10.66]

for c in range(0, 3):
    elemento = matriz[1][c] - ((25/9) * matriz[0][c])
    x.append(elemento)

# Temos agora que b = -0.958 e a = 0.45569

def p2x(x):
    resultado = (0.45569 * (x ** 2)) - 0.958 * x + 6.667
    return resultado

def p2y(y):
    # resultado = (0.45569 * (x ** 2)) - 0.958 * x + (6.667 - y)
    a = 0.45569
    b = -0.958
    c = 6.667 - y
    def raizes(a, b, c):
        delta = b ** 2 - (4 * a * c)
        raiz_delta = sqrt(delta)
        return raiz_delta
    raiz_delta = raizes(a, b, c)
    x1 = ((b * (-1)) + raiz_delta) / (2 * a)
    x2 = ((b * (-1)) - raiz_delta) / (2 * a)
    if x1 > 0:
        return x1
    if x2 > 0:
        return x2
    else:
        print('inválido')


p2x = p2x(7)

print(f'O polinomio resultante será: P2(x)=0.45569x²-0.958x+6.667')
print(f'No dia 07, a amostra atinge: {p2x:.2f}g')
print(f'Utilizando interpolação inversa, vimos que a amostra chegará a marca de 10g em: x= {p2y(10):.2f}')

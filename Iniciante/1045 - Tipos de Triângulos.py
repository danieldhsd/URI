valores = input().split()
valores = list(map(float, valores))
valores.sort(reverse=True)

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if a ** 2 == (b ** 2) + (c ** 2):
        print('TRIANGULO RETANGULO')
    if a ** 2 > (b ** 2) + (c ** 2):
        print('TRIANGULO OBTUSANGULO')
    if a ** 2 < (b ** 2) + (c ** 2):
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if ((a == b) and a != c) or ((a == c) and a != b) or ((b == c) and b != a):
        print('TRIANGULO ISOSCELES')

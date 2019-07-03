entrada = input().split(' ')
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

delta = (b ** 2) - (4 * a * c)

if delta < 0 or a == 0:
    print('Impossivel calcular')
    exit()

r1 = ((b * -1) + (delta ** 0.5)) / (2 * a)
r2 = ((b * -1) - (delta ** 0.5)) / (2 * a)

print('R1 = %.5f' % r1)
print('R2 = %.5f' % r2)

valor = float(input())
while valor < 0 or valor > 1000000.00:
    valor = float(input())

valor += 0.001
resto = 0

notas100 = int(valor / 100)
resto = valor - (notas100 * 100)

notas50 = int(resto / 50)
resto = resto - (notas50 * 50)

notas20 = int(resto / 20)
resto = resto - (notas20 * 20)

notas10 = int(resto / 10)
resto = resto - (notas10 * 10)

notas5 = int(resto / 5)
resto = resto - (notas5 * 5)

notas2 = int(resto / 2)
resto = resto - (notas2 * 2)

moedas1 = int(resto / 1)
resto = resto - (moedas1 * 1)

moedas50 = int(resto / 0.5)
resto = resto - (moedas50 * 0.5)

moedas25 = int(resto / 0.25)
resto = resto - (moedas25 * 0.25)

moedas10 = int(resto / 0.10)
resto = resto - (moedas10 * 0.10)

moedas5 = int(resto / 0.05)
resto = resto - (moedas5 * 0.05)

moedas01 = int(resto / 0.01)
resto = int(resto - (moedas01 * 0.01))

print("NOTAS:")
print(notas100, 'nota(s) de R$ 100.00')
print(notas50, 'nota(s) de R$ 50.00')
print(notas20, 'nota(s) de R$ 20.00')
print(notas10, 'nota(s) de R$ 10.00')
print(notas5, 'nota(s) de R$ 5.00')
print(notas2, 'nota(s) de R$ 2.00')
print("MOEDAS:")
print(moedas1, 'moeda(s) de R$ 1.00')
print(moedas50, 'moeda(s) de R$ 0.50')
print(moedas25, 'moeda(s) de R$ 0.25')
print(moedas10, 'moeda(s) de R$ 0.10')
print(moedas5, 'moeda(s) de R$ 0.05')
print(moedas01, 'moeda(s) de R$ 0.01')

valor = int(input())

while valor < 0:
    valor = int(input())

notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0
notas1 = 0
resto = 0

print(valor)

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

notas1 = int(resto / 1)
resto = resto - (notas1 * 1)

print(notas100, 'nota(s) de R$ 100,00')
print(notas50, 'nota(s) de R$ 50,00')
print(notas20, 'nota(s) de R$ 20,00')
print(notas10, 'nota(s) de R$ 10,00')
print(notas5, 'nota(s) de R$ 5,00')
print(notas2, 'nota(s) de R$ 2,00')
print(notas1, 'nota(s) de R$ 1,00')

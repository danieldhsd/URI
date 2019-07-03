casos_de_test = int(input())
lista = []
for i in range(casos_de_test):
    total_comida = float(input())
    dias = 0
    while total_comida > 1:
        dias += 1
        total_comida = total_comida / 2.0
    lista.append(dias)

for j in range(len(lista)):
    print(lista[j], 'dias')

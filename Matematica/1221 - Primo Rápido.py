def calcula_primo(numero):
    if numero >= 2:
        raiz_quadrada = int((numero ** 0.5) + 1)

        for index in range(2, raiz_quadrada):
            if numero % index == 0:
                return 'Not Prime'
        return 'Prime'
    else:
        return 'Not Prime'


casos_de_teste = int(input())

respostas = []

for i in range(casos_de_teste):
    numero = int(input())
    respostas.append(calcula_primo(numero))

for k in range(len(respostas)):
    print(respostas[k])

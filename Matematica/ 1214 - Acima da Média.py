casos_de_teste = int(input())

for i in range(casos_de_teste):
    entrada = input().split()
    soma = 0
    acimas_da_media = 0
    for j in range(1, int(entrada[0]) + 1):
        soma += int(entrada[j])

    media_nota_turma = soma / int(entrada[0])
    for k in range(1, int(entrada[0]) + 1):
        if int(entrada[k]) > media_nota_turma:
            acimas_da_media += 1
    media_de_alunos_acima_media = (acimas_da_media / int(entrada[0])) * 100

    print('{:.3f}%'.format(media_de_alunos_acima_media))

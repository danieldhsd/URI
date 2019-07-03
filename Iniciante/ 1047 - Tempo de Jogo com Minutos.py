valores = input().split(' ')
hora_comeco = int(valores[0])
minuto_comeco = int(valores[1])
hora_final = int(valores[2])
minuto_final = int(valores[3])

if hora_comeco > hora_final:
    hora_duracao = hora_final + 24 - hora_comeco
else:
    hora_duracao = hora_final - hora_comeco

if minuto_comeco > minuto_final:
    minuto_duracao = minuto_final + 60 - minuto_comeco
    hora_duracao -= 1
else:
    minuto_duracao = minuto_final - minuto_comeco


if hora_duracao == 0 and minuto_duracao == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(
        hora_duracao, minuto_duracao))

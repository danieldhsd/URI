dia_inicial = int(input().split()[1])
horario_inicial = input().split(':')
hora_inicio = int(horario_inicial[0])
minuto_inicio = int(horario_inicial[1])
segundo_inicio = int(horario_inicial[2])

dia_final = int(input().split()[1])
horario_final = input().split(':')
hora_final = int(horario_final[0])
minuto_final = int(horario_final[1])
segundo_final = int(horario_final[2])

dias_totais = dia_final - dia_inicial
horas_totais = hora_final - hora_inicio

if horas_totais < 0:
    horas_totais += 24
    dias_totais -= 1

minutos_totais = minuto_final - minuto_inicio

if minutos_totais < 0:
    minutos_totais += 60
    horas_totais -= 1

segundos_totais = segundo_final - segundo_inicio

if segundos_totais < 0:
    segundos_totais += 60
    minutos_totais -= 1

print('%d dia(s)' % dias_totais)
print('%d hora(s)' % horas_totais)
print('%d minuto(s)' % minutos_totais)
print('%d segundo(s)' % segundos_totais)

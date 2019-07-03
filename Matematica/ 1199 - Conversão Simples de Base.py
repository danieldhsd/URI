def decimal_to_hex(numero):
    return hex(numero)


def hex_to_decimal(numero):
    return int(str(numero), base=16)


lista = []

while True:
    numero = input()

    if len(numero) > 1 and numero[1] == 'x':
        resposta = hex_to_decimal(numero)

    elif int(numero) < 0:
        break

    elif int(numero) >= 0:
        resposta = decimal_to_hex(int(numero))
        resposta = resposta[:2] + resposta[2:].upper()

    lista.append(resposta)


for i in range(len(lista)):
    print(lista[i])

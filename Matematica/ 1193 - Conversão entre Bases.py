def decimal_to_bin(numero):
    return bin(numero)[2:]


def decimal_to_hex(numero):
    return hex(numero)[2:]


def bin_to_decimal(numero):
    return int(str(numero), base=2)


def bin_to_hex(numero):
    resp = bin_to_decimal(numero)
    return decimal_to_hex(resp)


def hex_to_decimal(numero):
    return int(str(numero), base=16)


def hex_to_bin(numero):
    resp = hex_to_decimal(numero)
    return decimal_to_bin(resp)


casos_de_test = int(input())

for i in range(casos_de_test):
    entrada = input().split()
    numero = entrada[0]
    base = entrada[1]

    if base == 'bin':
        resp1 = str(bin_to_decimal(int(numero))) + ' dec'
        resp2 = str(bin_to_hex(int(numero))) + ' hex'

    elif base == 'hex':
        resp1 = str(hex_to_decimal(numero)) + ' dec'
        resp2 = str(hex_to_bin(numero)) + ' bin'

    elif base == 'dec':
        resp1 = decimal_to_hex(int(numero)) + ' hex'
        resp2 = decimal_to_bin(int(numero)) + ' bin'

    print('Case {}:' .format(i + 1))
    print(resp1)
    print(resp2)
    print()

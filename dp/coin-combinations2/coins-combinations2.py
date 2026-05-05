import sys

sys.setrecursionlimit(1000000)

MOD = 10**9 + 7
M = {}

monedas = []


def coins(i, resto):
    # Llegamos al monto deseado, rama valida.
    if resto == 0:
        return 1
    # Nos quedamos sin monedas, o nos pasamos del monto buscado. Rama invalida.
    if i == len(monedas) or resto < 0:
        return 0

    if (i, resto) not in M:
        #                No se usa la moneda      Se usa la moneda (Puede repetir)
        M[(i, resto)] = (coins(i + 1, resto) + coins(i, resto - monedas[i])) % MOD

    return M[(i, resto)]


def solve():
    global monedas
    global M

    n, x = map(int, input().split())
    monedas = list(map(int, input().split()))

    result = coins(0, x)
    print(result)


solve()

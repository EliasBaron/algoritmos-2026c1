import sys

sys.setrecursionlimit(1000000)

MOD = 10**9 + 7
M = {}

monedas = []


def coins(i, suma):
    # Llegamos al monto deseado, rama valida.
    if suma == 0:
        return 1
    # Nos quedamos sin monedas, o nos pasamos del monto buscado. Rama invalida.
    if i == len(monedas) or suma < 0:
        return 0

    if (i, suma) not in M:
        #                No se usa la moneda      Se usa la moneda (Puede repetir)
        M[(i, suma)] = (coins(i + 1, suma) + coins(i, suma - monedas[i])) % MOD

    return M[(i, suma)]


def solve():
    global monedas
    global M

    n, x = map(int, input().split())
    monedas = list(map(int, input().split()))

    result = coins(0, x)
    print(result)


solve()

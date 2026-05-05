import sys

sys.setrecursionlimit(1000000)

MOD = 10**9 + 7
M = {}

monedas = []


def coins(resto):
    # Encontramos una solución valida, retornamos 1
    if resto == 0:
        return 1
    # Nos pasamos, rama invalida.
    if resto < 0:
        return 0

    if resto not in M:
        coincidencias = 0
        for moneda in monedas:
            coincidencias = (coincidencias + coins(resto - moneda)) % MOD

        M[resto] = coincidencias

    return M[resto]


def solve():
    global monedas
    global M

    n, x = map(int, input().split())
    monedas = list(map(int, input().split()))

    result = coins(x)
    print(result)


solve()

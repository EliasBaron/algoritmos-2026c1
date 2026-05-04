import sys

sys.setrecursionlimit(1000000)

MOD = 10**9 + 7
M = {}

monedas = []


def coins(suma):
    # Encontramos una solución valida, retornamos 1
    if suma == 0:
        return 1
    # Nos pasamos, rama invalida.
    if suma < 0:
        return 0

    if suma not in M:
        coincidencias = 0
        for moneda in monedas:
            coincidencias = (coincidencias + coins(suma - moneda)) % MOD

        M[suma] = coincidencias

    return M[suma]


def solve():
    global monedas
    global M

    n, x = map(int, input().split())
    monedas = list(map(int, input().split()))

    result = coins(x)
    print(result)


solve()

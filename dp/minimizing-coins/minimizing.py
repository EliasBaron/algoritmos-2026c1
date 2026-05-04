import sys

sys.setrecursionlimit(1000000)

INF = float("inf")
monedas = []
M = {}


def coins(restante):
    # Caso base: para formar suma 0 necesito 0 monedas.
    if restante == 0:
        return 0
    # Caso base: me pasé, rama inválida.
    if restante < 0:
        return INF

    if restante not in M:
        mejor = INF

        for moneda in monedas:
            mejor = min(mejor, 1 + coins(restante - moneda))

        M[restante] = mejor

    return M[restante]


def solve():
    global monedas
    global M

    n, x = map(int, input().split())
    monedas = list(map(int, input().split()))

    M.clear()

    result = coins(x)

    if result == INF:
        print(-1)
    else:
        print(result)


solve()

import sys

sys.setrecursionlimit(1000000)

INF = float("inf")

M = {}

w = []  # Pesos
v = []  # Valores

N = 0


# Queremos saber desde el elemento i, cual es la mayor cantidad que entra en una mochila con k peso restante.
def mochila(i, peso):
    # Casos base
    if peso < 0:
        return -INF  # Me pasé, mochila invalida.
    if peso == 0 or i == N:
        return 0  # En una mochila con peso 0 no entran más items o no tengo más items para agregar.

    # Recursión
    if (i, peso) not in M:
        M[(i, peso)] = max(mochila(i + 1, peso), v[i] + mochila(i + 1, peso - w[i]))

    return M[(i, peso)]


def reconstruct(i, peso):
    assert peso >= 0  # Aseguramos no caso invalido

    if peso == 0 or i == N:  # Caso base
        return []

    if mochila(i, peso) == mochila(i + 1, peso):
        return reconstruct(i + 1, peso)

    s = reconstruct(i + 1, peso - w[i])
    s.append(i)  # 0-indexed
    return s


def solve():
    global M, N, v, w

    n, k = map(int, input().split())
    N = n

    v = list(map(int, input().split()))
    w = list(map(int, input().split()))

    M.clear()

    result = mochila(0, k)
    solution = reconstruct(0, k)

    print(result)
    print(*solution)


solve()

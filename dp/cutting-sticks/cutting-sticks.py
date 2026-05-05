import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

INF = float("inf")
M = {}

cortes = []


# Costo minimo de realizar todos los cortes entre el indice i y el indice j del array de cortes.
def dp(i, j):
    # Caso base: no hay cortes que hacer entre i y j.
    if j - i <= 1:
        return 0
    if (i, j) not in M:
        longitud = cortes[j] - cortes[i]  # Costo de cualquier corte en este intervalo.
        minimo = INF
        # Probamos cada punto de corte intermedio entre i y j.
        for k in range(i + 1, j):
            minimo = min(minimo, longitud + dp(i, k) + dp(k, j))
        M[(i, j)] = minimo
    return M[(i, j)]


def solve():
    global cortes, M
    while True:
        L = int(input())
        if L == 0:
            break
        _ = int(input())
        puntos = list(map(int, input().split()))
        # Agregamos los extremos del palito como puntos ficticios.
        cortes = [0] + puntos + [L]
        M.clear()
        print(f"The minimum cutting is {dp(0, len(cortes) - 1)}.")


solve()

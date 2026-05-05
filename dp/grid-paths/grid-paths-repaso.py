import sys

sys.setrecursionlimit(1000000)
MOD = 10**9 + 7

M = {}

grid = []  # Representa la matriz de la grilla
N = 0


# Queremos saber la cantidad de caminos validos hasta el final, desde la posición (x, y) actual.
def paths(x, y):
    if x == N or y == N or grid[x][y] == "*":
        return 0  # No hay caminos validos hasta el final.

    if x == N - 1 and y == N - 1:
        return 1

    if (x, y) not in M:
        M[(x, y)] = (paths(x + 1, y) + paths(x, y + 1)) % MOD

    return M[(x, y)]


def reconstruct(x, y):
    # Caso feliz, llegué al final y no me tengo que mover más.
    if x == N - 1 and y == N - 1:
        return []

    # Recursión, hay al menos un camino valido yendo para abajo?
    if paths(x + 1, y) > 0:
        return ["D"] + reconstruct(x + 1, y)
    # Sino, voy por la derecha.
    return ["R"] + reconstruct(x, y + 1)


def solve():
    global N, grid, M
    N = int(input())
    grid = [input().strip() for _ in range(N)]
    M.clear()
    print(paths(0, 0))
    print(reconstruct(0, 0))


solve()

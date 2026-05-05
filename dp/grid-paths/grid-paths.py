import sys

sys.setrecursionlimit(1000000)

MOD = 10**9 + 7
M = {}

N = 0
maze = []


# Sumatoria de caminos validos para llegar hasta el final, desde las coordenadas x e y actuales.
def paths(x, y):
    # Si me fui del laberinto o encontré una trampa.
    if x == N or y == N or maze[x][y] == "*":
        return 0

    # LLegué al final, camino valido.
    if x == N - 1 and y == N - 1:
        return 1

    if (x, y) not in M:
        M[(x, y)] = (paths(x + 1, y) + paths(x, y + 1)) % MOD

    return M[(x, y)]


def reconstruct(x, y):
    if x == N - 1 and y == N - 1:
        return []
    # ¿Puedo ir abajo?
    if x + 1 < N and paths(x + 1, y) > 0:
        return ["D"] + reconstruct(x + 1, y)
    # Si no, voy a la derecha
    return ["R"] + reconstruct(x, y + 1)


def solve():
    global N, maze, M
    N = int(input())
    maze = [input().strip() for _ in range(N)]
    M.clear()
    print(paths(0, 0))
    print("".join(reconstruct(0, 0)))


solve()

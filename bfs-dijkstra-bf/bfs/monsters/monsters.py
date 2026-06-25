## multi-source BFS

import sys
from collections import deque
input = sys.stdin.readline

INF = float('inf')

# direcciones con su letra de movimiento
DIRS = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]


def bfs_monstruos(grid, monstruos, n, m):
    # multi-source BFS: arranca desde TODOS los monstruos a la vez.
    # dist[i][j] = pasos del monstruo más cercano hasta esa celda.
    dist = [[INF] * m for _ in range(n)]
    cola = deque()
    for mi, mj in monstruos:
        dist[mi][mj] = 0
        cola.append((mi, mj))
    while cola:
        i, j = cola.popleft()
        for di, dj, _ in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#' and dist[ni][nj] == INF:
                dist[ni][nj] = dist[i][j] + 1
                cola.append((ni, nj))
    return dist


def bfs_jugador(grid, start, dist_m, n, m):
    # BFS desde el jugador, con reconstrucción de camino (padre).
    # El jugador solo puede pisar una celda si llega ESTRICTAMENTE antes
    # que el monstruo más cercano: dist_jugador + 1 < dist_monstruo.
    dist = [[INF] * m for _ in range(n)]
    padre = [[None] * m for _ in range(n)]
    si, sj = start
    dist[si][sj] = 0
    cola = deque([(si, sj)])
    while cola:
        i, j = cola.popleft()
        for di, dj, c in DIRS:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#' and dist[ni][nj] == INF:
                if dist[i][j] + 1 < dist_m[ni][nj]:
                    dist[ni][nj] = dist[i][j] + 1
                    padre[ni][nj] = (i, j, c)
                    cola.append((ni, nj))
    return dist, padre


def solve():
    n, m = map(int, input().split())
    grid = [list(input().rstrip()) for _ in range(n)]

    # localizar al jugador (A) y a los monstruos (M)
    start = None
    monstruos = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'M':
                monstruos.append((i, j))

    # dos BFS
    dist_m = bfs_monstruos(grid, monstruos, n, m)
    dist_p, padre = bfs_jugador(grid, start, dist_m, n, m)

    # buscar una celda del borde alcanzable por el jugador
    destino = None
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                if dist_p[i][j] != INF:
                    destino = (i, j)
                    break
        if destino:
            break

    if destino is None:
        print("NO")
        return

    # reconstruir el camino desde el borde hacia atrás
    camino = []
    i, j = destino
    while padre[i][j] is not None:
        pi, pj, c = padre[i][j]
        camino.append(c)
        i, j = pi, pj
    camino.reverse()

    print("YES")
    print(len(camino))
    print(''.join(camino))


solve()
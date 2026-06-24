import sys
from collections import deque
input = sys.stdin.readline

DIRS = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

def dijkstra_01(grid, r, c, start, dest):
    INF = float('inf')
    dist = [[INF] * c for _ in range(r)]
    si, sj = start
    di0, dj0 = dest
    dist[si][sj] = 0
    dq = deque([(0, si, sj)])      # (distancia, i, j)
    
    while dq:
        d, i, j = dq.popleft()
        if d > dist[i][j]:          # entrada vieja, la salteo
            continue
        if (i, j) == (di0, dj0):    # llegué al destino, corto
            return d
        corriente = grid[i][j]
        for dir in range(8):
            di, dj = DIRS[dir]
            ni, nj = i + di, j + dj
            if 0 <= ni < r and 0 <= nj < c:
                costo = 0 if dir == corriente else 1
                nd = d + costo
                if nd < dist[ni][nj]:
                    dist[ni][nj] = nd
                    if costo == 0:
                        dq.appendleft((nd, ni, nj))
                    else:
                        dq.append((nd, ni, nj))
    return dist[di0][dj0]

def solve():
    while True:
        linea = input()
        if not linea:
            break
          
        r, c = map(int, linea.split())
        grid = []
        for _ in range(r):
            fila = input().strip()
            grid.append([int(x) for x in fila])
        
        q = int(input())
        resultados = []
        for _ in range(q):
            r1, c1, r2, c2 = map(int, input().split())
            # las coordenadas vienen en base 1, las paso a base 0
            start = (r1 - 1, c1 - 1)
            dest = (r2 - 1, c2 - 1)
            resultados.append(dijkstra_01(grid, r, c, start, dest))
        # imprimir resultados del caso
        for res in resultados:
            print(res)

solve()
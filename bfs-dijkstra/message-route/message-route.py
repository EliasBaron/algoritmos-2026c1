### BFS + Reconstrucción

import sys
from collections import deque

input = sys.stdin.readline


def message_route(grafo, origen, destino):
    n = len(grafo)
    dist = [-1] * (n + 1)
    padre = [-1] * (n + 1)

    dist[origen] = 0
    cola = deque([origen])

    while cola:
        nodo = cola.popleft()
        for vecino in grafo[nodo]:
            if dist[vecino] == -1:
                dist[vecino] = dist[nodo] + 1
                padre[vecino] = nodo
                cola.append(vecino)

    # Sin solución
    if dist[destino] == -1:
        return None

    # Reconstrucción
    camino = []
    actual = destino
    while actual != -1:
        camino.append(actual)
        actual = padre[actual]
    camino.reverse()
    return camino


def solve():
    n, m = map(int, input().split())

    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    sol = message_route(G, 1, n)

    if not sol:
        print("IMPOSSIBLE")
    else:
        print(len(sol))
        print(*sol)


solve()

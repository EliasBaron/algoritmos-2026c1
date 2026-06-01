import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

grafo = defaultdict(list)
visitado = set()
representantes = []


def dfs(nodo):
    visitado.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(vecino)


def solve():
    global visitado, representantes, grafo

    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, input().split())
        grafo[u].append(v)
        grafo[v].append(u)

    for nodo in range(1, N + 1):
        if nodo not in visitado:
            dfs(nodo)
            representantes.append(nodo)  # guardás uno por componente

    print(len(representantes) - 1)
    for i in range(len(representantes) - 1):
        print(representantes[i], representantes[i + 1])


solve()

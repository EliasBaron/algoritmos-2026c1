import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

grafo = defaultdict(list)
pila = []
visitado = set()


def dfs(nodo, grafo):
    visitado.add(nodo)
    for vecino in grafo[nodo]:
        if vecino not in visitado:
            dfs(vecino, grafo)
    pila.append(nodo)


def solve():
    global grafo, pila, visitado

    while True:
        N, M = map(int, input().split())
        if N == M == 0:
            break

        grafo = defaultdict(list)
        pila = []
        visitado = set()

        for _ in range(M):
            a, b = map(int, input().split())
            grafo[a].append(b)

        for nodo in range(1, N + 1):
            if nodo not in visitado:
                dfs(nodo, grafo)

        orden = pila[::-1]
        print(*orden)


solve()

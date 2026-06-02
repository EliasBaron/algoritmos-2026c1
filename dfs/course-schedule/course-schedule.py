import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

grafo = defaultdict(list)
pila = []
visitado = set()
en_pila = set()


def dfs(nodo, grafo):
    visitado.add(nodo)
    en_pila.add(nodo)

    for vecino in grafo[nodo]:
        if vecino in en_pila:  # ciclo!
            return False
        if vecino not in visitado:
            if not dfs(vecino, grafo):
                return False

    en_pila.remove(nodo)
    pila.append(nodo)
    return True


def solve():
    global grafo

    N, M = map(int, input().split())

    for _ in range(M):
        a, b = map(int, input().split())
        grafo[a].append(b)

    valid = True
    for nodo in range(1, N + 1):
        if nodo not in visitado:
            if not dfs(nodo, grafo):
                valid = False
                break

    orden = pila[::-1]

    if valid:
        print(*orden)
    else:
        print("IMPOSSIBLE")


solve()

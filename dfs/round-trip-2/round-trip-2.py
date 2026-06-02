import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

visitado = set()
en_pila = set()
padres = {}
ciclo = []


def dfs(nodo, grafo):
    visitado.add(nodo)
    en_pila.add(nodo)
    for vecino in grafo[nodo]:
        if ciclo:
            return
        if vecino not in visitado:
            padres[vecino] = nodo
            dfs(vecino, grafo)
        elif vecino in en_pila:
            actual = nodo
            while actual != vecino:
                ciclo.append(actual)
                actual = padres[actual]
            ciclo.append(vecino)
            ciclo.reverse()
            ciclo.append(ciclo[0])
    if not ciclo:
        en_pila.remove(nodo)


def solve():
    N, M = map(int, input().split())
    grafo = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        grafo[a].append(b)
    for nodo in range(1, N + 1):
        if nodo not in visitado:
            padres[nodo] = -1
            dfs(nodo, grafo)
        if ciclo:
            break
    if ciclo:
        print(len(ciclo))
        print(*ciclo)
    else:
        print("IMPOSSIBLE")


solve()

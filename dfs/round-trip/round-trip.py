import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

visited = set()
padre = {}
ciclo = []


def dfs(node, father, graph):
    visited.add(node)
    for neighbor in graph[node]:
        if ciclo:  # ya encontramos un ciclo, frenar todo
            return
        if neighbor not in visited:
            padre[neighbor] = node
            dfs(neighbor, node, graph)
        elif neighbor != father:
            # reconstruir el ciclo remontando padres
            actual = node
            while actual != neighbor:
                ciclo.append(actual)
                actual = padre[actual]
            ciclo.append(neighbor)
            ciclo.append(ciclo[0])  # cerrar el ciclo repitiendo el primero al final


def solve():
    global visited, padre, ciclo
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    for node in range(1, N + 1):
        if node not in visited:
            padre[node] = -1
            dfs(node, -1, graph)
        if ciclo:
            break

    if ciclo:
        print(len(ciclo))
        print(*ciclo)
    else:
        print("IMPOSSIBLE")


solve()

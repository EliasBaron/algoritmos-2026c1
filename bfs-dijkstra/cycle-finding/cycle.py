# Bellman-Ford

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find_negative_cycle(edges, n):
    dist = [0] * (n + 1)
    padre = [-1] * (n + 1)
    x = -1
    for _ in range(n):
        x = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                padre[v] = u
                x = v
        if x == -1:
            break

    if x == -1:
        return  # no hubo ciclo
    else:
        for _ in range(n):
            x = padre[x]

        ciclo = [x]
        actual = padre[x]
        while actual != x:
            ciclo.append(actual)
            actual = padre[actual]
        ciclo.append(x)

        ciclo.reverse()
        return ciclo


def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))

    ciclo = find_negative_cycle(edges, n)
    if ciclo is None:
        print("NO")
    else:
        print("YES")
        print(*ciclo)


solve()

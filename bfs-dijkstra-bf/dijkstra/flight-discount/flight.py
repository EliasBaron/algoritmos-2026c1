# Dijkstra con estados

import heapq
import sys

input = sys.stdin.readline

INF = float("inf")


def dijkstra(grafo, origen, destino, n):
    dist = [[INF] * 2 for _ in range(n + 1)]
    dist[origen][0] = 0
    heap = [(0, origen, 0)]  # (dist, nodo, cupón_usado)

    while heap:
        d, nodo, usado = heapq.heappop(heap)
        if d > dist[nodo][usado]:
            continue
        for vecino, peso in grafo[nodo]:
            if d + peso < dist[vecino][usado]:
                dist[vecino][usado] = d + peso
                heapq.heappush(heap, (d + peso, vecino, usado))
            if usado == 0 and d + peso // 2 < dist[vecino][1]:
                dist[vecino][1] = d + peso // 2
                heapq.heappush(heap, (d + peso // 2, vecino, 1))

    return min(dist[destino][0], dist[destino][1])


def solve():
    n, m = map(int, input().split())
    grafo = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        grafo[a].append((b, c))

    print(dijkstra(grafo, 1, n, n))


solve()

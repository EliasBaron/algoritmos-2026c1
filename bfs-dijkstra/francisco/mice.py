"""
Author: Francisco Soulignac
Time in UVA: 0s

Solución: Dijkstra con las aristas del revés empezando de la salida
"""

import heapq
import sys

input = sys.stdin.readline

INF = 1 << 28


def dijkstra(G, src):
    dist = [INF] * len(G)
    q = [(0, src)]
    while q:
        d, u = heapq.heappop(q)
        if dist[u] < INF:
            continue
        dist[u] = d
        for w, v in G[u]:
            if dist[v] == INF:
                heapq.heappush(q, (d + w, v))
    return dist


def main():
    c = int(input())
    for i in range(c):
        input()

        n, e, t, m = int(input()), int(input()), int(input()), int(input())

        G = [[] for _ in range(n + 1)]
        for _ in range(m):
            u, v, w = map(int, input().split())
            G[v].append((w, u))  # aristas al revés
        res = dijkstra(G, e)
        print(sum(1 for d in res if d <= t))
        if i < c - 1:
            print()


main()

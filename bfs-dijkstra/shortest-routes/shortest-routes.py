import heapq
import sys

input = sys.stdin.readline


INF = float("inf")


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


def solve():
    n, m = map(int, input().split())

    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        G[u].append((w, v))

    print(*dijkstra(G, 1)[1:])


solve()

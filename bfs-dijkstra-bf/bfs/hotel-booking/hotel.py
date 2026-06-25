import sys
from collections import defaultdict, deque
import heapq

input = sys.stdin.readline

def dijkstra(src, graph, n):
    dist = [float('inf')] * (n + 1)
    dist[src] = 0
    heap = [(0, src)]
    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(heap, (dist[v], v))
    return dist

def solve():
    while True:
        n = int(input())
        if n == 0:
            break

        # Leer hoteles
        line = list(map(int, input().split()))
        h = line[0]
        hotels = line[1:h+1]  # ciudades con hotel

        # Leer grafo
        m = int(input())
        graph = defaultdict(list)
        for _ in range(m):
            a, b, t = map(int, input().split())
            graph[a].append((b, t))
            graph[b].append((a, t))

        # Nodos relevantes: ciudad 1, hoteles, ciudad n
        relevant = [1] + hotels + [n]
        # Eliminar duplicados manteniendo orden
        seen = set()
        relevant_unique = []
        for r in relevant:
            if r not in seen:
                seen.add(r)
                relevant_unique.append(r)
        relevant = relevant_unique

        # Índice de cada nodo relevante en el grafo reducido
        idx = {city: i for i, city in enumerate(relevant)}
        R = len(relevant)

        # Dijkstra desde cada nodo relevante
        # y construir grafo reducido donde hay arista si dist <= 600
        red_graph = defaultdict(list)
        for city in relevant:
            dist = dijkstra(city, graph, n)
            for other in relevant:
                if other != city and dist[other] <= 600:
                    red_graph[idx[city]].append(idx[other])

        # BFS en grafo reducido desde idx[1] hasta idx[n]
        src = idx[1]
        dst = idx[n]

        visited = [-1] * R
        visited[src] = 0
        queue = deque([src])

        while queue:
            u = queue.popleft()
            for v in red_graph[u]:
                if visited[v] == -1:
                    visited[v] = visited[u] + 1
                    queue.append(v)

        if visited[dst] == -1:
            print(-1)
        else:
            # visited[dst] = cantidad de pasos (días)
            # hoteles reservados = días - 1 (no se cuenta ni origen ni destino)
            print(visited[dst] - 1)

solve()
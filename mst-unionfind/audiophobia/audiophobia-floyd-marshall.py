import sys
input = sys.stdin.readline
INF = 1 << 28

def solve():
    number_case = 0
    while True:
        line = input()
        if not line:
            break
        parts = line.split()
        if len(parts) < 3:
            continue
        c, s, q = map(int, parts)
        if c == s == q == 0:
            break
        number_case += 1

        # matriz dist[i][j], inicializar en INF, diagonal en 0
        dist = [[INF] * (c + 1) for _ in range(c + 1)]
        for i in range(c + 1):
            dist[i][i] = 0

        for _ in range(s):
            u, v, w = map(int, input().split())
            dist[u][v] = w
            dist[v][u] = w

        # Floyd-Warshall minimax
        for k in range(1, c + 1):
            dk = dist[k]
            for i in range(1, c + 1):
                di = dist[i]
                dik = di[k]
                if dik >= INF:        # si i no llega a k, no sirve de escala
                    continue
                for j in range(1, c + 1):
                    nuevo = dik if dik > dk[j] else dk[j]   # max(di[k], dk[j])
                    if nuevo < di[j]:
                        di[j] = nuevo

        # output
        if number_case > 1:
            print()
        print(f"Case #{number_case}")
        for _ in range(q):
            a, b = map(int, input().split())
            if dist[a][b] >= INF:
                print("no path")
            else:
                print(dist[a][b])

solve()

solve()
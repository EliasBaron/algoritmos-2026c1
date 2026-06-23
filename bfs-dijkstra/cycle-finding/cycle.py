def solve():
    n, m = map(int, input().split())

    G = [[] for _ in range(n + 1)]

    for _ in range(m):
        v, w, d = map(int, input().split())
        G[v].append((w, d))


solve()

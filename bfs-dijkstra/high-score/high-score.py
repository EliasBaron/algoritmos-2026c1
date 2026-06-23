import sys
input = sys.stdin.readline
MINF = float('-inf')

def dists_from(G, src, n):
    dist = [MINF] * (n + 1)
    dist[src] = 0
    process = [src]
    changed = [False] * (n + 1)
    for _ in range(n):
        if not process:
            break
        for w in process:
            changed[w] = False
        prev, process = process, []
        for v in prev:
            for w, d in G[v]:
                if dist[w] < dist[v] + d:
                    dist[w] = dist[v] + d
                    if not changed[w]:
                        process.append(w)
                    changed[w] = True
    return dist, changed

def solve():
    n, m = map(int, input().split())
    
    F = [[] for _ in range(n + 1)]  # normal
    B = [[] for _ in range(n + 1)]  # invertido
    
    for _ in range(m):
        v, w, d = map(int, input().split())
        F[v].append((w, d))
        B[w].append((v, d))
        
    dist_f, changed_f = dists_from(F, 1, n)
    dist_b, changed_b = dists_from(B, n, n)
    for v in range(1, n + 1):
        if changed_f[v] and dist_b[v] != MINF:
            print(-1)
            return
    print(dist_f[n])

solve()
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
        for w in process:        # reseteo los flags de los nodos de esta ronda
            changed[w] = False
        prev, process = process, []   # prev = a procesar, process = nuevo (vacío)
        for v in prev:           # por cada nodo que cambió antes
            for w, d in G[v]:    # miro sus aristas
                if dist[w] < dist[v] + d:   # si mejora (maximiza)
                    dist[w] = dist[v] + d
                    if not changed[w]:      # si no lo agregué ya esta ronda
                        process.append(w)   # lo proceso la próxima
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
import sys
input = sys.stdin.readline

def find_negative_cycle(G, n):
    dist = [0] * (n + 1)
    padre = [-1] * (n + 1)
    changed = [False] * (n + 1)
    
    process = list(range(1, n + 1))
    for w in process:
        changed[w] = False

    x = -1
    for _ in range(n):
        if not process:
            break
        for w in process:
            changed[w] = False
        prev, process = process, []
        for v in prev:
            for w, d in G[v]:
                if dist[w] > dist[v] + d:
                    dist[w] = dist[v] + d
                    padre[w] = v
                    if not changed[w]:
                        process.append(w)
                    changed[w] = True

    # lo que quedó en process después de N rondas está en ciclo negativo
    if not process:
        return None

    # agarramos cualquier nodo que sigue cambiando y remontamos el ciclo
    x = process[0]
    for _ in range(n):
        x = padre[x]  # garantiza que x está dentro del ciclo

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
    G = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        G[a].append((b, c))

    ciclo = find_negative_cycle(G, n)
    if ciclo is None:
        print("NO")
    else:
        print("YES")
        print(*ciclo)

solve()
import sys
from collections import deque

input = sys.stdin.readline

def mx(G, f, t):
    dist = [-1] * (len(G) + 1)

    dist[f] = 0
    cola = deque([f])
    
    while cola:
        node = cola.popleft()
        for v in G[node]:
            if dist[v] == -1:
                dist[v] = dist[node] + 1
                cola.append(v)
    
    return dist[t]
            

def solve():
    t = int(input())
    
    for caso in range(t):
        if caso > 0:
            print()
            
        n = int(input())
        
        G = [[] for _ in range(n)]
        for _ in range(n):
            partes = list(map(int, input().split()))
            c = partes[0]
            vecinos = partes[2:]
            G[c] = vecinos
        
        c1, c2 = map(int, input().split())
        
        intermediates = mx(G, c1, c2) - 1  # Se le resta 1 para convertir la
                         				   # distancia en intermerdiarios
        print(c1, c2, intermediates)
  
                                 
solve()
import sys
import heapq

input = sys.stdin.readline
INF = 1 << 28

sys.setrecursionlimit(1000000)

def min_sound(G, src, dest):
  dist = [INF] * len(G)
  q = [(0, src)]
  
  while q:
    d, u = heapq.heappop(q)
    if dist[u] < INF:
      continue
    dist[u] = d
    for w, v in G[u]:
      if dist[v] == INF:
        heapq.heappush(q, (max(d,w), v))
  
  return dist[dest]
    


def solve():
  number_case = 1
  
  while True:
    line = input()
    if not line:        # EOF
        break
    line = line.split()
    if len(line) < 3:   # línea en blanco, la salteo
        continue
    c, s, q = map(int, line)
    if c == s == q == 0:
        break
    
    print(f"Case #{number_case}")

    G = [[] for _ in range(c + 1)]
    for _ in range(s):
      c1, c2, d = map(int, input().split())
      G[c1].append((d, c2))
      G[c2].append((d, c1))
    
    for _ in range(q):
      fr, to =  map(int, input().split())
      
      res = min_sound(G, fr, to)
      
      if res != INF:
        print(res)
      else:
        print('no path')
    
    number_case += 1
    print()  

solve()
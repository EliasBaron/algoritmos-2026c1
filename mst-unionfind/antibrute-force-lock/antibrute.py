import sys
from itertools import combinations

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

class UF:
    def __init__(self, n):
        self.p = list(range(n))   # iota: cada uno es su raíz
        self.s = [1] * n

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])   # path compression
        return self.p[v]

    def unite(self, v, w):
        rv, rw = self.find(v), self.find(w)
        if rv == rw:
            return
        if self.s[rv] < self.s[rw]:
            rv, rw = rw, rv
        self.p[rw] = rv
        self.s[rv] += self.s[rw]

def costo(a, b):
    total = 0
    for i in range(4):
        d = abs(a[i] - b[i])
        total += min(d, 10 - d)
    return total

def solve():
    t = int(input())
    
    for _ in range(t):
        line = list(map(int, input().split()))
        
        n = line[0]
        combs = [[0,0,0,0]] + [list(map(int, str(line[i+1]).zfill(4))) for i in range(n)]
		
        E = []
        for i, j in combinations(range(n + 1), 2):
            E.append((costo(combs[i], combs[j]), i, j))
        E.sort()

        uf = UF(n + 1)
        result = 0
        for c, v, w in E:
            if uf.find(v) != uf.find(w):
                result += c
                uf.unite(v, w)

        print(result)

solve()
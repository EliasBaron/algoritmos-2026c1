# Kruskal, se ordenan las aristas por costo, se recorre de menor a mayor y se usa union find.

import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.s = [1] * n

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def unite(self, v, w):
        vv, vw = self.find(v), self.find(w)
        if vv == vw:
            return

        if self.s[vw] < self.s[vv]:
            vv, vw = vw, vv
        self.p[vw] = vv
        self.s[vv] += self.s[vw]


def solve():
    n, m = map(int, input().split())

    E = []
    for _ in range(m):
        v, w, c = map(int, input().split())
        E.append((c, v, w))
    E.sort()

    uf = UF(n + 1)

    result = 0
    e = 0
    for c, v, w in E:
        if uf.find(v) != uf.find(w):
            result += c
            e += 1  # Sumo a la cantidad total conexiones realizadas entre componentes disconexas.
            uf.unite(v, w)

    # El MST necesita n-1 aristas, si no logre conectar todas las componentes (Todas las ciudades) entonces tengo un grafo disconexo. O sea, es imposible la solución.
    if e < n - 1:
        print("IMPOSSIBLE")
    else:
        print(result)


solve()

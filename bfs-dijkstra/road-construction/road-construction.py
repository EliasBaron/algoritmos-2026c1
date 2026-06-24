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

    L = []
    for _ in range(m):
        v, w = map(int, input().split())
        L.append((v, w))

    uf = UF(n + 1)

    number_components = n
    max_size = 1
    for v, w in L:
        if uf.find(v) != uf.find(w):
            uf.unite(v, w)
            number_components = number_components - 1
            max_size = max(
                max_size, uf.s[uf.find(v)]
            )  # Hago la comparación con la raiz de v, ya que en las raices es en donde está el valor del size correcto.
        print(number_components, max_size)


solve()

import sys
from collections import deque
input = sys.stdin.readline
INF = 1 << 28


class UF:
    def __init__(self, n):
        self.p = list(range(n))
        self.s = [1] * n

    def find(self, v):
        while self.p[v] != v:
            self.p[v] = self.p[self.p[v]]   # path halving (iterativo, sin recursión)
            v = self.p[v]
        return v

    def unite(self, v, w):
        rv, rw = self.find(v), self.find(w)
        if rv == rw:
            return False
        if self.s[rv] < self.s[rw]:
            rv, rw = rw, rv
        self.p[rw] = rv
        self.s[rv] += self.s[rw]
        return True


def max_en_camino(mst, origen, destino, n):
    # BFS sobre el árbol desde origen hasta destino,
    # llevando la arista máxima cruzada para llegar a cada nodo.
    if origen == destino:
        return 0
    visitado = [False] * (n + 1)
    max_hasta = [0] * (n + 1)
    visitado[origen] = True
    cola = deque([origen])
    while cola:
        u = cola.popleft()
        if u == destino:
            return max_hasta[u]
        for v, peso in mst[u]:
            if not visitado[v]:
                visitado[v] = True
                # el cuello de botella hasta v es el max entre lo que traía y esta arista
                max_hasta[v] = max(max_hasta[u], peso)
                cola.append(v)
    return INF   # no hay camino (destino en otra componente)


def solve():
    number_case = 0
    out = []
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

        # leer aristas
        edges = []
        for _ in range(s):
            u, v, w = map(int, input().split())
            edges.append((w, u, v))   # peso primero para ordenar
        edges.sort()

        # Kruskal: construir el MST guardando el árbol como lista de adyacencia
        uf = UF(c + 1)
        mst = [[] for _ in range(c + 1)]
        usadas = 0
        for w, u, v in edges:
            if uf.unite(u, v):        # solo si conecta componentes distintas
                mst[u].append((v, w))
                mst[v].append((u, w))
                usadas += 1
                if usadas == c - 1:   # el MST ya está completo
                    break

        # responder consultas con un BFS sobre el árbol
        if number_case > 1:
            out.append("")            # línea en blanco entre casos
        out.append(f"Case #{number_case}")
        for _ in range(q):
            a, b = map(int, input().split())
            res = max_en_camino(mst, a, b, c)
            if res >= INF:
                out.append("no path")
            else:
                out.append(str(res))

    sys.stdout.write('\n'.join(out) + '\n')


solve()
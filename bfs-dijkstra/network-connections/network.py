# Union find

import sys
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


def solve():
    data = sys.stdin.read().split('\n')
    idx = 0
    casos = int(data[idx]); idx += 1
    salida = []

    for c in range(casos):
        # saltear líneas en blanco antes del caso
        while idx < len(data) and data[idx].strip() == '':
            idx += 1

        n = int(data[idx]); idx += 1
        uf = UF(n + 1)
        exitos, fracasos = 0, 0

        # leer operaciones hasta que se acabe el caso
        while idx < len(data) and data[idx].strip() != '':
            partes = data[idx].split()
            idx += 1
            if not partes:
                break
            tipo, i, j = partes[0], int(partes[1]), int(partes[2])
            if tipo == 'c':
                uf.unite(i, j)
            else:  # 'q'
                if uf.find(i) == uf.find(j):
                    exitos += 1
                else:
                    fracasos += 1

        salida.append(f"{exitos},{fracasos}")

    print('\n\n'.join(salida))

solve()
import sys

sys.setrecursionlimit(1000000)
INF = float("inf")

M = {}


# Cantidad de pasos MINIMOS para llegar a 0 restando cualquiera de los digitos del numero actual.
def digits(n):
    if n < 0:
        return INF  # Rama invalida, retornamos el neutro, INF en el caso de min.

    if n == 0:
        return 0  # Desde 0, me toma 0 pasos llegar al 0

    if n not in M:
        cs = list(str(n))
        minimo = INF

        for c in cs:
            if int(c) == 0:  # Atajo caso de recursión infinita
                continue
            minimo = min(minimo, 1 + digits(n - int(c)))
        M[n] = minimo

    return M[n]


def solve():
    n = int(input())
    print(digits(n))


solve()

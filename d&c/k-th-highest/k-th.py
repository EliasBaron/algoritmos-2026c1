import sys
from bisect import bisect_left

input = sys.stdin.readline

# def count(X):
#     print(f"? {X}")
#     sys.stdout.flush()  # importante: forzar que el juez reciba la pregunta
#     return int(input())
#
# # qué es lo que minimizás/maximizás?
# la cantidad de puntajes superiores a uno dado.
#
# cuál es el rango lo y hi?
# lo es 1, ya que puede ser desde 1 y hi son TODOS los posibles por enunciado
#
# cómo escribís la función condicion?
# count(mid) >= K. O sea: "¿hay al menos K elementos mayores o iguales a mid?". Si es verdad, mid podría ser la respuesta o algo más chico. Si es falso, mid es muy chico y hay que subir.

suiza = []
finlandia = []


def count(X):
    return (len(finlandia) - bisect_left(finlandia, X)) + (
        len(suiza) - bisect_left(suiza, X)
    )


def solve():
    K = int(input())

    low = 1
    hi = 10**9

    while low < hi:
        mid = (low + hi) // 2
        if count(mid) >= K:
            hi = mid
        else:
            low = mid + 1

    print(f"! {low}")
    sys.stdout.flush()


solve()

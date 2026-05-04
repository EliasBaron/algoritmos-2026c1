import sys

input = sys.stdin.readline

N = 0
manzanas = []


def backtracking(next_manzana=0, sum_grupo_1=0, sum_grupo_2=0):
    global N
    global manzanas

    if next_manzana == N:
        return abs(sum_grupo_1 - sum_grupo_2)

    # Opción A: Manzana en grupo 1
    left = backtracking(
        next_manzana + 1, sum_grupo_1 + manzanas[next_manzana], sum_grupo_2
    )

    # Opción B: Manzana en grupo 2
    right = backtracking(
        next_manzana + 1, sum_grupo_1, sum_grupo_2 + manzanas[next_manzana]
    )

    return min(left, right)


def solve():
    global N
    global manzanas

    N = int(input())
    manzanas = list(map(int, input().split()))

    result = backtracking()
    print(result)


solve()

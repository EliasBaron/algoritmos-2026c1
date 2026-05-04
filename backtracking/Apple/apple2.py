import sys

input = sys.stdin.readline

N = 0
manzanas = []
restantes = []
mejor = float("inf")


def backtracking(next_manzana=0, sum_grupo_1=0, sum_grupo_2=0):
    global N
    global manzanas
    global restantes
    global mejor

    diferencia_actual = abs(sum_grupo_1 - sum_grupo_2)
    suma_restante = restantes[next_manzana]

    # Poda:
    # aunque usemos todas las manzanas restantes para achicar la diferencia,
    # no podemos mejorar la mejor respuesta actual.
    if (diferencia_actual - suma_restante) >= mejor:
        return mejor

    if next_manzana == N:
        mejor = min(mejor, diferencia_actual)
        return diferencia_actual

    left = backtracking(
        next_manzana + 1, sum_grupo_1 + manzanas[next_manzana], sum_grupo_2
    )

    right = backtracking(
        next_manzana + 1, sum_grupo_1, sum_grupo_2 + manzanas[next_manzana]
    )

    return min(left, right)


def solve():
    global N
    global manzanas
    global restantes
    global mejor

    N = int(input())
    manzanas = list(map(int, input().split()))

    mejor = float("inf")
    restantes = [0] * (N + 1)

    for i in range(N - 1, -1, -1):
        restantes[i] = restantes[i + 1] + manzanas[i]

    result = backtracking()
    print(result)


solve()

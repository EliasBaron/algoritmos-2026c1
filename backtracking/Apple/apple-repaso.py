import sys

N = 0
apples = []


# Queremos desde la manzana i, la repartición con menor diferencia entre ponerla en el grupo 1 al grupo 2.
def split(i, cant_grupo_1, cant_grupo_2):
    # Si ya colocamos todas las manzanas, entonces retorno la diferencia entre los grupos.
    if i == len(apples):
        return abs(cant_grupo_1 - cant_grupo_2)

    # Recursión
    apple_weight = apples[i]
    return min(
        split(i + 1, cant_grupo_1 + apple_weight, cant_grupo_2),  # Coloco en el grupo 1
        split(i + 1, cant_grupo_1, cant_grupo_2 + apple_weight),  # Coloco en el grupo 2
    )


def solve():
    global N
    global apples

    N = int(input())
    apples = list(map(int, input().split()))

    result = split(0, 0, 0)
    print(result)


solve()

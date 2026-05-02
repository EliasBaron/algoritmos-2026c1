import sys

duration = []  # duraciones de cada pista
N = 0  # largo de la cinta
tracks = 0  # cantidad de pistas


def backtracking(next_track=0, value=0, elegidas=None):
    if elegidas is None:
        elegidas = []

    # CASO BASE 1: nos pasamos del largo de la cinta, descartamos la rama
    if value > N:
        return (0, [])

    # CASO BASE 2: llegamos al final de las pistas O llenamos la cinta exacto
    # (poda: si llenamos exacto no puede haber nada mejor, cortamos)
    if next_track == tracks or value == N:
        return (value, elegidas)

    # Opción A: NO incluir la pista next_track
    left = backtracking(next_track + 1, value, elegidas)

    # Opción B: SÍ incluir la pista next_track
    right = backtracking(
        next_track + 1, value + duration[next_track], elegidas + [next_track]
    )

    # Nos quedamos con la que tenga mayor suma
    return left if left[0] > right[0] else right


for line in sys.stdin:
    line = line.split()
    if not line:
        continue

    N = int(line[0])
    tracks = int(line[1])
    duration = [int(x) for x in line[2 : 2 + tracks]]

    best_val, best_tracks = backtracking()
    result = [str(duration[i]) for i in best_tracks]
    print(" ".join(result) + " sum:" + str(best_val))

import sys

input = sys.stdin.readline

N = 0
K = 0
casillas_blancas = []
casillas_negras = []


def backtracking(indice, puestos, diagonales_1=None, diagonales_2=None):
    global K

    if diagonales_1 is None and diagonales_2 is None:
        diagonales_1 = set()
        diagonales_2 = set()

    # Caso base: Ya colocamos todos los alfiles.
    if puestos == K:
        return 1
    # Caso base: Llegamos al final del tablero.
    if indice == len(casillas):
        return 0

    # Poda: Quedan menos espacios que alfiles por colocar.
    if K - puestos > len(casillas) - indice:
        return 0

    fila, columna = casillas[indice]
    total = 0

    # Rama 1: no colocar
    total += backtracking(indice + 1, puestos, diagonales_1, diagonales_2)

    # Rama 2: intentar colocar, si las diagonales están libres
    diag1 = fila - columna
    diag2 = fila + columna
    if diag1 not in diagonales_1 and diag2 not in diagonales_2:
        # creamos sets nuevos con la diagonal agregada, sin modificar los originales
        total += backtracking(
            indice + 1,
            puestos + 1,
            diagonales_1 | {diag1},  # pyright: ignore[reportOptionalOperand]
            diagonales_2 | {diag2},  # pyright: ignore[reportOptionalOperand]
        )
    return total


def solve():
    global N, K, casillas
    while True:
        line = input().split()
        N, K = int(line[0]), int(line[1])
        if N == 0 and K == 0:
            break
        # armamos las casillas blancas y negras
        for fila in range(N):
            for columna in range(N):
                if (fila + columna) % 2 == 0:
                    casillas_blancas.append((fila, columna))
                else:
                    casillas_negras.append((fila, columna))
        print(backtracking(0, 0))


solve()

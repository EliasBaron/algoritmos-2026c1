import sys

input = sys.stdin.readline

N = 0


def puede_colocar(ficha_izq, ficha_der):
    return ficha_izq[1] == ficha_der[0]


def backtracking(actual, disponibles, derecha, fichas_puestas=0):
    global N
    if fichas_puestas == N and puede_colocar(actual, derecha):
        return True
    for i, disponible in enumerate(disponibles):
        nuevas = disponibles[:i] + disponibles[i + 1 :]
        if puede_colocar(actual, disponible):
            if backtracking(disponible, nuevas, derecha, fichas_puestas + 1):
                return True
        disponible_reversed = disponible[::-1]
        if puede_colocar(actual, disponible_reversed):
            if backtracking(disponible_reversed, nuevas, derecha, fichas_puestas + 1):
                return True
    return False


def solve():
    global N
    while True:
        N = int(input())
        if N == 0:
            break
        m = int(input())
        izquierda = tuple(map(int, input().split()))
        derecha = tuple(map(int, input().split()))
        disponibles = [tuple(map(int, input().split())) for _ in range(m)]

        if backtracking(izquierda, disponibles, derecha):
            print("YES")
        else:
            print("NO")


solve()

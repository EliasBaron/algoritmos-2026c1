import sys
from math import sqrt

input = sys.stdin.readline

N = 0  # cantidad de numeros


def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def backtracking(elegidos=None, candidatos=None):
    if elegidos is None:
        elegidos = [1]
    if candidatos is None:
        candidatos = set(range(2, N + 1))

    if len(elegidos) + 1 == N:
        ultimo = next(iter(candidatos))
        if es_primo(elegidos[-1] + ultimo) and es_primo(1 + ultimo):
            print(" ".join(str(x) for x in elegidos + [ultimo]))
            return

    for candidato in range(2, N + 1):  # el 1 ya está fijo
        if candidato not in elegidos:
            if es_primo(elegidos[-1] + candidato):
                # lo agregamos y seguimos
                backtracking(elegidos + [candidato], candidatos - {candidato})


def solve():
    global N
    case_num = 1
    for line in sys.stdin:
        if case_num > 1:
            print()
        print(f"Case {case_num}:")
        line = line.strip()
        if not line:
            continue
        N = int(line)
        backtracking()
        case_num += 1


solve()

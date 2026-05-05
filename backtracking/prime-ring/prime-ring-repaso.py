import math
import sys

N = 0


def is_prime(n):
    # Prime numbers must be greater than 1
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # All other even numbers are not prime
    if n % 2 == 0:
        return False

    # Check for odd divisors starting from 3 up to sqrt(n)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True


# Con una lista de numeros dados, quiero saber que numero puedo conectar siguiente para formar el anillo.
def ring(siguientes, anillo):
    # Caso base final, ya agregué todo al anillo, y queda ver si el ultimo conecta con 1 (Es valido)
    if len(anillo) == N:
        if is_prime(anillo[-1] + 1):
            print(" ".join(str(x) for x in anillo))
            return

    for i, actual in enumerate(siguientes):
        if is_prime(actual + anillo[-1]):
            resto_siguientes = siguientes[:i] + siguientes[i + 1 :]
            ring(resto_siguientes, anillo + [actual])


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
        ring(list(range(2, N + 1)), [1])
        case_num += 1


solve()

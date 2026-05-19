import sys

input = sys.stdin.readline


def existe_cuadrado(grid, N, M, k, L, U):
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            if grid[i][j] >= L and grid[i + k - 1][j + k - 1] <= U:
                return True
    return False


def solve():
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().split())))

        Q = int(input())
        for _ in range(Q):
            L, U = map(int, input().split())

            # búsqueda binaria sobre k
            low, high = 0, min(N, M)
            while high > low + 1:
                mid = (low + high) // 2
                if existe_cuadrado(grid, N, M, mid, L, U):
                    low = mid  # mid sirve, intento agrandar
                else:
                    high = mid  # mid no sirve, achico

            # verifico si low o high es válido
            if existe_cuadrado(grid, N, M, high, L, U):
                print(high)
            elif existe_cuadrado(grid, N, M, low, L, U):
                print(low)
            else:
                print(0)

        print("-")


solve()

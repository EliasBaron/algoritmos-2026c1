import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline

grid = []
N, M, lower_bound, upper_bound = 0, 0, 0, 0


def existe_cuadrado(k):
    for i in range(N - k + 1):
        for j in range(M - k + 1):
            if grid[i][j] >= lower_bound and grid[i + k - 1][j + k - 1] <= upper_bound:
                return True
    return False


def solve():
    global grid, N, M, lower_bound, upper_bound

    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break

        grid = []
        for _ in range(N):
            grid.append(list(map(int, input().split())))

        Q = int(input())
        for _ in range(Q):
            lower_bound, upper_bound = map(int, input().split())

            # búsqueda binaria sobre k
            low, high = 0, min(N, M)
            while low < high:
                mid = (low + high + 1) // 2
                if existe_cuadrado(mid):
                    low = mid  # mid sirve, intento agrandar
                else:
                    high = mid - 1  # mid no sirve, achico

            print(low)

        print("-")


solve()


# def existe_cuadrado(k):
#     for i in range(N - k + 1):
#         fila_sup = grid[i]          # fila superior del cuadrado
#         fila_inf = grid[i + k - 1]  # fila inferior del cuadrado

#         # primera j donde la esquina sup-izq >= L
#         j_min = bisect_left(fila_sup, lower_bound)

#         # última j donde la esquina inf-der <= U
#         # bisect_right da el índice después del último <= U
#         j_max = bisect_right(fila_inf, upper_bound) - k

#         # si j_min <= j_max, existe al menos una columna válida
#         if j_min <= j_max:
#             return True
#     return False

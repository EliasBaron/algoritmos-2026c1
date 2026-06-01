import sys

sys.setrecursionlimit(1000000)

visited = set()
grid = []
N = 0
M = 0


def dfs(i, j):
    visited.add((i, j))

    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for di, dj in direcciones:
        ni, nj = i + di, j + dj

        if (
            0 <= ni < N
            and 0 <= nj < M
            and (ni, nj) not in visited
            and grid[ni][nj] == "."
        ):
            dfs(ni, nj)


def solve():
    global visited, grid, N, M

    N, M = map(int, input().split())

    grid = [input().strip() for _ in range(N)]

    rooms = 0
    for i in range(N):
        for j in range(M):
            if (i, j) not in visited and grid[i][j] == ".":
                dfs(i, j)
                rooms += 1

    print(rooms)


solve()

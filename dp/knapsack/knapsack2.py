import sys

sys.setrecursionlimit(10**6)


input = sys.stdin.readline

NEG_INF = -(10**18)

M = {}
N = 0

# items = [(0, 0), (value, weight), ...]
items = []


def knapsack(i, amount):
    if amount < 0:
        return NEG_INF
    if i == N:  # ya no quedan items
        return 0
    if (i, amount) not in M:
        value, weight = items[i]
        M[(i, amount)] = max(
            knapsack(i + 1, amount),
            value + knapsack(i + 1, amount - weight),
        )
    return M[(i, amount)]


def reconstruct(i, amount):
    if i == N:
        return []
    if knapsack(i, amount) == knapsack(i + 1, amount):
        return reconstruct(i + 1, amount)
    s = reconstruct(i + 1, amount - items[i][1])
    s.append(i)  # 0-indexed
    return s


def solve():
    global items
    global M

    n, k = map(int, input().split())

    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    items = list(zip(values, weights))

    M.clear()

    result = knapsack(0, k)
    solution = reconstruct(0, k)

    print(result)
    print(*solution)


solve()

import sys

input = sys.stdin.readline

NEG_INF = -(10**18)

M = {}

# items[0] es dummy
# items = [(0, 0), (value, weight), ...]
items = []


def knapsack(i, amount):
    if amount < 0:
        return NEG_INF

    if i == 0 or amount == 0:
        return 0

    if (i, amount) not in M:
        value, weight = items[i]

        M[(i, amount)] = max(
            knapsack(i - 1, amount),  # no tomar item i
            value + knapsack(i - 1, amount - weight),  # tomar item i
        )

    return M[(i, amount)]


def reconstruct(i, amount):
    if amount < 0:
        raise Exception("Solución inválida")
    if i == 0:
        return []

    if knapsack(i, amount) == knapsack(i - 1, amount):
        return reconstruct(i - 1, amount)

    s = reconstruct(i - 1, amount - items[i][1])
    s.append(i)
    return s


def solve():
    global items
    global M

    n, k = map(int, input().split())

    values = list(map(int, input().split()))
    weights = list(map(int, input().split()))

    items = [(0, 0)] + list(zip(values, weights))

    M.clear()

    result = knapsack(n, k)
    solution = reconstruct(n, k)

    print(result)
    print(*solution)


solve()

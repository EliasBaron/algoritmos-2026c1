import sys

sys.setrecursionlimit(1000000)


INF = float("inf")

M = {}

# books =  [(price, pages)]
books = []


# Queremos devolver, el numero maximo de paginas que podemos llevarnos con un monto dado.
def book(i, amount):
    if amount < 0:
        return -INF
    if i == len(books):
        return 0

    if (i, amount) not in M:
        M[(i, amount)] = max(
            book(i + 1, amount), books[i][1] + book(i + 1, amount - books[i][0])
        )

    return M[(i, amount)]


def solve():
    global books
    global M

    n, x = map(int, input().split())

    prices = list(map(int, input().split()))
    pages = list(map(int, input().split()))

    books = list(zip(prices, pages))

    M.clear()

    result = book(0, x)
    print(result)


solve()

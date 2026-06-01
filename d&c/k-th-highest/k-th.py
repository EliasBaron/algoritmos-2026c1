import sys
from bisect import bisect_left

input = sys.stdin.readline


# def count(X):
#     return (len(finlandia) - bisect_left(finlandia, X)) + (
#         len(suiza) - bisect_left(suiza, X)
#     )


def count(X):
    print(f"? {X}")
    sys.stdout.flush()  # importante: forzar que el juez reciba la pregunta
    return int(input())


def solve():
    K = int(input())

    low = 1
    hi = 10**9

    while low < hi:
        mid = (low + hi) // 2
        if count(mid) >= K:
            hi = mid
        else:
            low = mid + 1

    print(f"! {low}")
    sys.stdout.flush()


solve()

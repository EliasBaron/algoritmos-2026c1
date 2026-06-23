from collections import deque


def sliding_window_min(arr, k):
    dq = deque()  # guarda índices
    result = []
    for i, x in enumerate(arr):
        # sacar elementos fuera de la ventana
        while dq and dq[0] < i - k + 1:
            dq.popleft()
        # mantener orden creciente: sacar los mayores
        while dq and arr[dq[-1]] >= x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result


def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(*sliding_window_min(arr, k))


solve()

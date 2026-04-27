import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

INF = float('inf')
v = []
p = []
M = {}

def mochila(i, k):
    if k < 0:
        return -INF
    if k == 0 or i == 0:
        return 0
    if (i, k) not in M:
        M[(i, k)] = max(mochila(i - 1, k), v[i] + mochila(i - 1, k - p[i]))
    return M[(i, k)]

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())

        v.clear()
        p.clear()
        M.clear()

        v.append(0)
        p.append(0)

        for _ in range(n):
            pi, wi = map(int, input().split())
            v.append(pi)
            p.append(wi)

        g = int(input())
        people = [int(input()) for _ in range(g)]

        total = 0
        for mw in people:
            total += mochila(n, mw)

        print(total)
main()
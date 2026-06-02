import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

color = {}
graph = defaultdict(list)


def dfs(node, c, graph):
    color[node] = c
    for neighbord in graph[node]:
        if neighbord not in color:
            if not dfs(neighbord, 1 - c, graph):
                return False
        elif color[neighbord] == c:
            return False
    return True


def solve():
    global color, graph

    while True:
        V = int(input())
        if V == 0:
            break

        color = {}
        graph = defaultdict(list)

        # leer aristas hasta 0 0
        while True:
            u, v = map(int, input().split())
            if u == 0 and v == 0:
                break
            graph[u].append(v)
            graph[v].append(u)

        is_claw = True
        for node in range(1, V + 1):
            if node not in color:
                if not dfs(node, 0, graph):
                    is_claw = False
                    break
        if is_claw:
            print("YES")
        else:
            print("NO")


solve()

import sys
from collections import defaultdict

sys.setrecursionlimit(1000000)

team = {}
graph = defaultdict(list)


def dfs(pupil, t, graph):
    team[pupil] = t
    for neighbord in graph[pupil]:
        if neighbord not in team:
            if not dfs(neighbord, 3 - t, graph):
                return False
        elif team[neighbord] == t:
            return False
    return True


def solve():
    global graph

    n, m = map(int, input().split())
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    possible = True
    for node in range(1, n + 1):
        if node not in team:
            if not dfs(node, 1, graph):
                possible = False
                break

    if possible:
        print(*[team[i] for i in range(1, n + 1)])
    else:
        print("IMPOSSIBLE")


solve()

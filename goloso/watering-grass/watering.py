import math


def amount_to_cover(sprinklers, w):
    position = 0
    count = 0
    i = 0
    while position < w:
        best = position
        while i < len(sprinklers) and sprinklers[i][0] <= position:
            best = max(best, sprinklers[i][1])
            i += 1
        if best == position:
            # imposible cubrir
            break
        position = best
        count += 1
    return (position >= w, count)


def solve():
    n, l, w = map(int, input().split())
    sprinklers = []
    for _ in range(n):
        pos, rad = map(int, input().split())
        half = w / 2
        if rad <= half:
            continue
        alcance = math.sqrt(rad**2 - half**2)
        sprinklers.append((pos - alcance, pos + alcance))
    sprinklers.sort()
    result = amount_to_cover(sprinklers, l)
    if result[0]:
        print(result[1])
    else:
        print(-1)


solve()

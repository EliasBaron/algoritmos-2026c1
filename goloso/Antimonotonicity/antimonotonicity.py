def longest_alternating(fred):
    mary = [fred[0]]
    need_low = True
    for i in range(1, len(fred)):
        if need_low and fred[i] < mary[-1]:
            mary.append(fred[i])
            need_low = False
        elif not need_low and fred[i] > mary[-1]:
            mary.append(fred[i])
            need_low = True
    return len(mary)


def solve():
    T = int(input())
    for _ in range(T):
        data = list(map(int, input().split()))
        fred = data[1:]
        print(longest_alternating(fred))


solve()

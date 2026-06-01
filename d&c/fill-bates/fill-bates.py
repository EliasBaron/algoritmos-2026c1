from bisect import bisect_left
from collections import defaultdict

S = input()
Q = int(input())

pos = defaultdict(list)
for i, c in enumerate(S):
    pos[c].append(i)

for _ in range(Q):
    SS = input().strip()

    cur = 0
    start = -1
    end = -1
    matched = True

    for c in SS:
        if c not in pos:
            matched = False
            break

        idx = bisect_left(pos[c], cur)

        if idx == len(pos[c]):
            matched = False
            break

        found_at = pos[c][idx]

        if start == -1:
            start = found_at
        end = found_at
        cur = found_at + 1

    if matched:
        print(f"Matched {start} {end}")
    else:
        print("Not matched")

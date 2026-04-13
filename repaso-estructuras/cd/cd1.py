import sys

for line in sys.stdin:
    N, M = map(int, line.split())
    
    if N == 0 and M == 0:
        break
    
    jack = [int(input()) for _ in range(N)]
    jill = [int(input()) for _ in range(M)]
    
    coincidences = 0
    i, j = 0, 0
    
    while i < N and j < M:
        if jack[i] == jill[j]:
            coincidences += 1
            i += 1
            j += 1
        elif jack[i] < jill[j]:
            i += 1
        else:
            j += 1
    
    print(coincidences)
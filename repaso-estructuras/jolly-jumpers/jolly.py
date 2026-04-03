import sys

for line in sys.stdin:
    nums = list(map(int, line.split()))
    n = nums[0]
    seq = nums[1:]
    
    if n == 1:
        print("Jolly")
        continue
    
    visto = set()
    for i in range(1, n):
        diff = abs(seq[i] - seq[i-1])
        if 1 <= diff <= n-1:
            visto.add(diff)
    
    requerido = set(range(1, n))
    print("Jolly" if visto == requerido else "Not jolly")
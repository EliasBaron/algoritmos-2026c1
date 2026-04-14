import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    
    events = []
    
    for _ in range(n):
        a, b = map(int, input().split())
        events.append((a, 1))   # entra
        events.append((b, -1))  # sale
    
    events.sort(key=lambda x: (x[0], x[1]))
    
    max_customers = current = 0
    
    for i in range(len(events)):
        current += events[i][1]
        max_customers = max(max_customers, current)
    
    print(max_customers)

solve()
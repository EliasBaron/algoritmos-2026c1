import sys
input = sys.stdin.readline

def solve():
    while (True):
        N, M = map(int, input().split())
        
        if (N == M == 0):
            break
        
        jackCDs = set()
        jillCDs = set()
            
        for _ in range(N):
            jackCDs.add(int(input()))
            
        for _ in range(M):
            jillCDs.add(int(input()))
        
        print(len(jackCDs & jillCDs))
    
solve()
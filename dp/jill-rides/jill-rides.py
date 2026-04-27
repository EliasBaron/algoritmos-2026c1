import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

INF = float('inf')

n = []
M = {}

def dp(i):
    if i == 1:
        return (n[1], 1)
    
    if i not in M:
        prev_sum, prev_start = dp(i-1)
        
        if prev_sum + n[i] >= n[i]:
            M[i] = (prev_sum + n[i], prev_start)
        else:
            M[i] = (n[i], i)
    
    return M[i]

def comp(cand, best):
    # cand y best: (suma, inicio, fin)
    
    if cand[0] > best[0]:
        return True
    if cand[0] < best[0]:
        return False
    
    # empate en suma → mayor longitud
    cand_len = cand[2] - cand[1]
    best_len = best[2] - best[1]
    
    if cand_len > best_len:
        return True
    if cand_len < best_len:
        return False
    
    # empate en longitud → menor inicio
    return cand[1] < best[1]

def main():
    t = int(input())
    
    for caso in range(1, t + 1):
        s = int(input())
        
        global n, M
        n = [0]
        M.clear()
        
        for _ in range(s - 1):
            n.append(int(input()))
        
        best = (-INF, 0, 0)
        
        for i in range(1, len(n)):
            suma, inicio = dp(i)
            cand = (suma, inicio, i)
            
            if comp(cand, best):
                best = cand
        
        if best[0] <= 0:
            print(f"Route {caso} has no nice parts")
        else:
            print(f"The nicest part of route {caso} is between stops {best[1]} and {best[2] + 1}")

main()
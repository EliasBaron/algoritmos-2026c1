import sys
input = sys.stdin.readline

def solve():
  T = int(input())
  
  for _ in range(T):
    n = int(input())
    seen = {}
    
    izq = 0
    maxCoincidences = 0
    
    for i in range(n):
      z = int(input())
      
      if z in seen:  #Existe en el dic
        izq = max(izq, seen[z] + 1)
      seen[z] = i
      maxCoincidences = max(maxCoincidences, i - izq + 1)
      
    print(maxCoincidences)
    
solve()
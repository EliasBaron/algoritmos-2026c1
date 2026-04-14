import heapq

import sys
input = sys.stdin.readline

def solve():
  
  def insert(heap,x):
    heapq.heappush(heap,x)
    ex.append(f"insert {x}")
    
  def pop(heap):
    heapq.heappop(heap)
    ex.append("removeMin")
    
  heap = []
  ex = []
  
  n = int(input())
  
  for _ in range(n):
    parts = input().split()
    cm = parts[0]        # string con el comando
    if (cm != "removeMin"):
      x = int(parts[1])    # el número
      
    match cm:
      case "insert":
        insert(heap, x)
      case "removeMin":
        if (heap): 
          pop(heap)
        else: 
          insert(heap, 0)
          pop(heap)
      case "getMin":
        while(heap and heap[0] < x):
          pop(heap)
        if(not heap or x < heap[0]):
            insert(heap,x)
        ex.append(f"getMin {x}")
  
  print(len(ex))
  print('\n'.join(ex))

solve()
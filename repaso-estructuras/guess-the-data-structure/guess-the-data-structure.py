### Para este problema, recibimos primero un "n", el cual indica la cantidad de instrucciones que se recibiran a continuación, luego "n" ordenes de agregado y sacado de numeros. En base al orden del ordenado y sacado de los elementos, debemos determinar si se trata de un stack (lifo), queue (fifo), pq (always largers first), impossible (no puede ser ninguno), not sure (pueden ser varios)

from collections import deque
import heapq

import sys
input = sys.stdin.readline

def solve():
  while True:
    try:
      n = int(input())
    except:
      break #EOF
    
    isStack, isQueue, isPQ = True, True, True
    
    stack, pq  = [], []
    queue = deque()
        
    for _ in range(n):
      tc, nm = map(int, input().split())
      
      match tc:
        case 1:
          if (isStack):
            stack.append(nm)
          if (isQueue):
            queue.append(nm)
          if (isPQ):
            heapq.heappush(pq, -nm)
        case 2:
          if (isStack):
            isStack = (len(stack) > 0 and (stack.pop() == nm))
          if (isQueue):
            isQueue = (len(queue) > 0 and  queue.popleft() == nm)
          if (isPQ):
            isPQ = (len(pq) and -heapq.heappop(pq) == nm)
            
    match isStack, isQueue, isPQ:
      case True, False, False:
        print("stack")
      case False, True, False:
        print("queue")    
      case False, False, True:
        print("priority queue")
      case False, False, False:
        print("impossible")
      case _ :
        print("not sure")
    
solve()
import sys
input = sys.stdin.readline

def solve():
  n = int(input())
  
  l = list(map(int, input().split()))
  stack = []  # Stack (valor,posición)
  ans   = []
  
  for i in range(n):
    while (stack and stack[-1][0] >= l[i]):   #Se sacan los mayores
      stack.pop()
    if stack : ans.append(stack[-1][1]+1)
    else: ans.append(0)
    stack.append((l[i], i))
  
  print(*ans)
solve()
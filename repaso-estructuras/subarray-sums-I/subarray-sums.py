import sys
input = sys.stdin.readline

def solve():
  n, x = map(int, input().split())
  freq = {0:1}
  P = 0
  count = 0
  
  arr = map(int, (input().split()))
  
  for num in arr:
    P += num
    count += freq.get(P - x, 0)
    freq[P] = freq.get(P, 0) + 1
    
  print(count)
  
solve()
## Dado un string "s", tenemos que pensar cuantas veces "se repite" el bloque minimo que forma s. Por ejemplo: "abcd" = 1, "aaaa" = 4, "ababab" = 3.

import sys
input = sys.stdin.readline

def solve():
  
  def zarray(s):
    n = len(s)
    z = [n] * n
    l, r = 0, 1
    for i in range(1, n):
        z[i] = min(z[i - l], r - i)
        if z[i] < r - i:
            continue
        l = i
        while r < n and s[r - l] == s[r]:
            r += 1
        z[i] = r - l
        if r == i:
            r += 1
    return z
  
  while(True):
    string = input().strip()
    if (string == "."):
      break
    
    z = zarray(string)
    n = len(string)
    largest = 1
    
    for i in range(1,n):
      if (i + z[i] == n and n % i == 0):
        largest = max(largest, int(n/i))
    
    print(largest)

solve()
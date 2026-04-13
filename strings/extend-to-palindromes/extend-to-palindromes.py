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
  
  for string in sys.stdin:
    string = string.strip()
    if not string:
      break
    
    reversedString = string[::-1]
    z = zarray(reversedString + "$" + string)
    n = len(string)
    
    maxCoincidence = 0
    for i in range(n+1, len(z)):
      if (z[i] + i == len(z)):
        maxCoincidence = max(maxCoincidence,z[i])
    
    final = string+(string[:n - maxCoincidence])[::-1]
    print(final)

solve()
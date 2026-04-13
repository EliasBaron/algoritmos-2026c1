# En este problema, primero se recibe un numero T, especificando la cantidad de test cases a resolver. Luego, en T lineas, se reciben los strings a evaluar si son palindromos, alindromos o normales. Para cada caso de test, se devuelve en una sola linea la palabra correspondiente al caso con "alindrome", "palindrome" o "simple".

#Obs: un string es palindromo cuando para todos sus caracteres a(i) son iguales a a(d-i+1) (1 <= i <= d). Y un alindromo es el resultado de la concatenación de dos palindromos.

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
  
  def isPalindrome(string):
     return string == string[::-1]
    
  def isAlindrome(string):
    n = len(string)
    rev = string[::-1]

    # construcciones
    A = string + '#' + rev
    B = rev + '#' + string

    zA = zarray(A)
    zB = zarray(B)

    pref_pal = [False]*(n+1)
    suf_pal = [False]*(n+1)

    # prefijos palindromos
    for i in range(n):
        if zA[n+1+i] == n-i:
            pref_pal[n-i] = True

    # sufijos palindromos
    for i in range(n):
        if zB[n+1+i] == n-i:
            suf_pal[i] = True

    # probar cortes
    for i in range(1, n):
        if pref_pal[i] and suf_pal[i]:
            return True

    return False
  
  T = int(input())
  
  for _ in range(T):
    string = input().strip()
    
    if (isAlindrome(string)):
      print("alindrome")
    elif (isPalindrome(string)):
      print("palindrome")
    else: print("simple")
    
solve()
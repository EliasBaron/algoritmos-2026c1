## Ok, se recibe basicamente un string, y se debe tratar de encontrar los patrones que lo conforman, y esos k periodicos que lo conforman, los mas chicos. Por ejemplo, para "abcabcabcabc", se podría tomar "abc" x3, "abcabc" x6, "abcabcabcabc" x12 en el caso de que se tomene todos, pero se busca la conformación con la menor cantidad de caracteres, en este caso "abc".

# Se tiene el string, se aplica la función z array y con esa lista, tenemos que trabajar para descular. Seguimos el mismo calculo con los bordes, si tenemos un string, que el valor de z + indice = tamaño del string, se puede entonces que el string se repite cada i veces, con la diferencia que, para ver si es un k valido, tengo que ver si puedo dividir el string por la longitud del k (por ejemplo, hohoho (6) no es divisible por 4) y de esos k candidatos quedarme siempre con el minimo.

import sys
input = sys.stdin.readline

def solve():
  
  def zarray(string):
    z=[]
    for i in range(len(string)):
      if i == 0:
          z.append(0)
          continue
      
      rightString = string[i:]
      coincidences = 0
      for k in range(len(rightString)):
        if rightString[k] != string[k]:
          break
        else: coincidences += 1
        
      z.append(coincidences)
    return z

  T = int(input())

  for _ in range(T):
    input()  # linea en blanco
    string = input().strip()
    z = zarray(string)
    
    smallestPeriod = len(string)
    
    for i in range(len(string)):
      if (z[i] + i == len(string) and len(string) % i == 0):
        smallestPeriod = min(smallestPeriod, i)  
    
    print(smallestPeriod)
    if _ < T - 1:
      print() # Separación entre respuestas
  
solve()
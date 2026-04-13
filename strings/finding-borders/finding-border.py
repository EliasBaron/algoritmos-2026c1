# Se pide, encontrar el borde izquierdo y el borde derecho del string, para luego, calcular sus tamaños y devolverlos. Un borde es un prefijo que también es sufijo pero sin ser el string completo.

# Por ejemplo:
# El zarray de abcababcab sería [0,1,0,2,1,5,0,0,2,0] siendo correspondientes 2 al borde izquierdo y 5 al borde derecho, entonces se puede decir que, la longitud del borde izquierdo es el numero en el z array más alto en la mitad de la longitud de la lista, y el numero del borde derecho es el mas alto de la otra mitad de la lista.

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

  string = input().strip()
  z = zarray(string)
  
  bordersLengths = []
  
  for i in range(len(z)):
    if (z[i]+i == len(string)):
      bordersLengths.append(z[i])
  
  bordersLengths.sort()
  print(*bordersLengths)
  
solve()
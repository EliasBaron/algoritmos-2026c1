# En la primer linea de entrada se recibe un string de tamño "n" y en la segunda linea se recibe un patrón de longitud "m". Se debe imprimir un entero, el cual corresponde a la cantidad de ocurrencias del patrón en el string.

# Tenemos que concatenar las dos entradas, patrón$string , y luego utilizando zarray que genera una lista donde cada indice contiene la cantidad de coincidencias de lo siguiente con el string total, luego debemos devolver la cantidad de entradas donde el numero del indice corresponda a la longitud del patrón recibido (m)

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
  patron = input().strip()
  
  concatenatedString = patron+"$"+string
  
  z = zarray(concatenatedString)
  
  matches = 0
  for i in range(len(z)):
    if z[i] == len(patron):
      matches += 1
  
  print(matches)
  
solve()
  

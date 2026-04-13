# En este problema, primero recibo T, que denota la cantidad de test cases a resolver. Luego, recibo una linea con dos numeros "N" y "M", los cuales son los largos correspondientes a las dos siguientes listas a recibir. Por ultimo, en dos lineas separadas, recibo los "N" y "M" que conforman la lista.

# Estrategia, puedo recorrer la primer lista e ingresar todos los numeros y coincidencias en un hash clave valor (numero, coincidencias), inicializo un contador de elementos a eliminar, y luego recorro la segunda lista, los elementos que simplemente no están en el hash, suman uno al contador de elementos a eliminar, y luego, para los que si están, resto la cantidad de coincidencias al valor de coincidencias en el hash. Finalmente, sumo todos los ABSOLUTOS de los valores de coincidencia que me quedaron en el hash a la cantidad a quitar.

import sys
input = sys.stdin.readline

def solve():
  
  T = int(input())
  
  for _ in range(T):
    n, m = map(int, input().split())
    
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
  
    presentElems = {}
    
    for i in range(0,n):
      presentElems[l1[i]] = presentElems.get(l1[i], 0) + 1
      
    for i in range(0,m):
      presentElems[l2[i]] = presentElems.get(l2[i], 0) - 1
      
    print(sum(abs(v) for v in presentElems.values()))
    
solve()
    
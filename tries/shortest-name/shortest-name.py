# Primero recibo el numero de T casos. Cada caso inicia con una linea de un numero "n", el cual representa la gente de la aldea. Cada una de las siguientes "n" líneas van a contener un string representando el nombre de cada aldeano. Se necesita que se devuelva el numero de total de caracteres necesarios para llamar por el nombre a todos los aldeanos.

# Estrategía: Primero insertar todos los nombres de los aldeanos en el trie, el cual guarda un valor por defecto 0 y letras. Haciendo que, cada arista representando la conexión con las letras contabilice la cantidad de veces que una letra para una palabra insertada pasó por ahí digamos. Por lo cual, luego en la busqueda, tengo que hacer una suma de las veces que se pasa por cada letra hasta llegar a un nodo que tiene como valor 1 (Ya que como fue pasado una vez sola, es el prefijo más corto para un nombre)

import sys
input = sys.stdin.readline

def solve():
  
  #Trie:
  tree = [{}]
  
  def insert(name):
    cur = 0
    for c in name:
      if c not in tree[cur]:
        tree[cur][c] = [len(tree), 1]
        tree.append({})
      else: tree[cur][c][1] += 1
      cur = tree[cur][c][0]
  
  def search(name):
    cur = 0
    curSum = 0
    for c in name:
      if c not in tree[cur]:
        return 0
      elif tree[cur][c][1] == 1:
        return curSum + 1
      curSum += 1
      cur = tree[cur][c][0]
    return curSum
  
  T = int(input())
  
  for _ in range(T):
    n = int(input())
    tree = [{}]
    
    # -- Insertar palabras en el trie y luego acumulamos.
    nameList = []
    for _ in range(n):
      name = input()
      nameList.append(name)
      insert(name)
    

    # -- Iteramos sobre los nombres recibidos y vamos acumulando.
    total = 0
    for name in nameList:
      total += search(name)
        
    print(int(total))
    
solve()
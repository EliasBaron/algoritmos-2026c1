# Basicamente en este problema, recibo hasta 100000 entradas para el diccionario, una fila en blanco y un mensaje de hasta 100000 palabras (Una por fila también). El mensaje es una secuencia de palabras en el idioma extranjero y debo devolver el significado de cada una en ingles a medida que van siendo ingresadas.

# Estrategia: Guardar en el trie, en donde se tiene como valor por defecto el string "eh" todos los caracteres correspondientes a las palabras en el idioma extranjero, y en el nodo que representa el final de una palabra extranjera, guardar el string en ingles correspondiente a la palabra traducida. Entonces, luego de guardar todas las entradas del diccionario, ir buscando las palabras que voy recibiendo en el try, y devolver el valor guardado del nodo en donde quedo (Si es que existe, sino también devuelvo eh)

import sys
input = sys.stdin.readline


def solve():
  
  # Trie:
  tree = [["", {}]]
  
  def insert(word, meaning):
    cur = 0
    for c in word:
      if c not in tree[cur][1]:
        tree[cur][1][c] = len(tree)
        tree.append(["",{}])
      cur = tree[cur][1][c]
    tree[cur][0] = meaning
    
  def search(word):
    cur = 0
    for c in word:
      if c not in tree[cur][1]:
        return "eh"
      cur = tree[cur][1][c]
    return tree[cur][0] if tree[cur][0] != "" else "eh" 
    
  # --- Guardar las palabras en el Trie ---
  while True:
    line = input().split()
    if not line:
      break
    meaning, word = line[0], line[1]
    insert(word, meaning)
      
  for line in sys.stdin:
    foreignWord = line.strip()
    print (search(foreignWord))
      
      
solve()
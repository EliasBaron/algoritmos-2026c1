# El problema es el siguiente. Recibimos primero en una linea un entero m, el cual contiene la cantidad de palabras en el Hay Point dictionary, y un n, el numero de descripciones de trabajo a recibir. Luego, las siguientes m filas, contienen una palabra y un valor en dolares. Luego de eso, las n descripciones de empleo, las cuales están separadas por una linea conteniendo un periodico.

# Se busca devolver, para cada descripcion de trabajo, el salario correspondiente a la suma de los valores segun Hay Point para todas las palabras que aparecen en la descripción, siendo que si no está la palabra suma 0.

#Estrategia: Primero, recibir la las m palabras con los valores, y guardarlas en un trie, en el cual, cada nodo va a tener el valor de la palabra basicamente (siendo 0 por defecto), entonces, se van a ir sumando nodos con letras, y en las letras finales que cierran una palabra, el valor de nodo va a contener el valor de la palabra. Entonces, luego, reciben las n descripciones de trabajos, que son listas de strings, y cada string va a recorrer el try, guardando la suma total para cada descripción y devolviendola al terminar de recorrer la lista de palabras.

import sys
input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())

    # --- Trie ---
    # Cada nodo: [valor, {char: indice_hijo}]
    # valor = 0 por defecto
    tree = [[0, {}]]

    def insert(word, value):
        cur = 0
        for c in word:
            if c not in tree[cur][1]:
                tree[cur][1][c] = len(tree)
                tree.append([0, {}])
            cur = tree[cur][1][c]
        tree[cur][0] = value  # guardamos el valor en el nodo final

    def search(word):
        cur = 0
        for c in word:
            if c not in tree[cur][1]:
                return 0
            cur = tree[cur][1][c]
        return tree[cur][0]

    # --- Insertar en el trie ---
    for _ in range(m):
        parts = input().split()
        word, value = parts[0], float(parts[1])
        insert(word, value)

    # --- Leer descripciones ---
    for _ in range(n):
        total = 0
        while True:
            line = input().split()
            if line == ["."]:
                break
            for word in line:
                total += search(word)
        print(int(total))

solve()
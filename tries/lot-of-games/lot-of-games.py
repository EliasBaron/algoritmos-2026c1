import sys
from collections import defaultdict
input = sys.stdin.readline

WIN  = 0
LOSE = 1

def solve():
    n, k = map(int, input().split())

    # --- Construcción del Trie ---
    # Cada nodo: (es_terminal, {char: indice_hijo})
    tree = [(False, {})]  # nodo raíz en índice 0

    def insert(s):
        cur = 0
        for c in s:
            children = tree[cur][1]
            if c not in children:
                children[c] = len(tree)
                tree.append((False, {}))
            cur = children[c]
        # marcar terminal
        is_term, ch = tree[cur]
        tree[cur] = (True, ch)

    for _ in range(n):
        insert(input().strip())

    # --- Calcular forces[WIN][i] y forces[LOSE][i] ---
    # Recorremos de atrás hacia adelante (los hijos siempre tienen índice mayor)
    # porque insert() siempre agrega hijos con índice > padre
    size = len(tree)
    forces = [[False] * size, [False] * size]  # forces[WIN/LOSE][nodo]

    for i in range(size - 1, -1, -1):
        is_term, children = tree[i]

        if not children:
            # Nodo hoja: el que llega acá no puede mover → pierde
            # canWin = False (no puedo ganar desde acá)
            # canLose = True  (sí puedo "lograr" perder, porque ya perdí)
            forces[WIN][i]  = False
            forces[LOSE][i] = True
        else:
            # Para WIN: ¿existe algún hijo donde el rival NO pueda ganar?
            forces[WIN][i]  = any(not forces[WIN][child]  for child in children.values())
            # Para LOSE: ¿existe algún hijo donde el rival SÍ pueda perder?
            forces[LOSE][i] = any(    forces[LOSE][child] for child in children.values())

    can_win  = forces[WIN][0]
    can_lose = forces[LOSE][0]

    # --- Meta-juego con k partidas ---
    if not can_win:
        # Primero nunca puede ganar → Segundo gana siempre
        print("Second")
    elif can_lose:
        # Primero puede ganar Y perder → control total
        # Estrategia: pierde las k-1 primeras, gana la k-ésima
        print("First")
    else:
        # Primero siempre gana (no puede perder a propósito)
        # El resultado alterna: partida 1 gana First, partida 2 gana Second, ...
        # → gana el que empieza la última partida, que depende de la paridad de k
        print("First" if k % 2 == 1 else "Second")

solve()
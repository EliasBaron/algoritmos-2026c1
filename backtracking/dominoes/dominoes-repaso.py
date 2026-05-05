N = 0  # Num de espacios


# Quiero saber, si hay solución posible, sabiendo la ficha de la izquierda y la ultima de la derecha. Tengo que colocar m fichas
# en el medio para ganar la partida.
def dominoes(ficha_izq, colocadas, disponibles, ficha_der):
    # Caso feliz. Me coloqué todas las fichas y tengo que validar que sea una solución valida.
    if colocadas == N:
        return ficha_izq[1] == ficha_der[0]

    # Ya no tengo más fichas para colocar, no puedo llegar a la solución.
    if not disponibles:
        return False

    # Recursión, verificar si puedo colocar una ficha como está o de revés.
    for i, ficha in enumerate(disponibles):
        resto_fichas = disponibles[:i] + disponibles[i + 1 :]

        if ficha_izq[1] == ficha[0]:
            if dominoes(ficha, colocadas + 1, resto_fichas, ficha_der):
                return True

        reversed_ficha = ficha[::-1]
        if ficha_izq[1] == reversed_ficha[0]:
            if dominoes(reversed_ficha, colocadas + 1, resto_fichas, ficha_der):
                return True

    return False


def solve():
    global N
    while True:
        N = int(input())
        if N == 0:
            break
        m = int(input())
        izquierda = tuple(map(int, input().split()))
        derecha = tuple(map(int, input().split()))
        disponibles = [tuple(map(int, input().split())) for _ in range(m)]

        if dominoes(izquierda, 0, disponibles, derecha):
            print("YES")
        else:
            print("NO")


solve()

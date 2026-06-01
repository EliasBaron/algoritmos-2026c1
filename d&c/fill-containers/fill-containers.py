import sys


def puede_llenar(vasijas, m, capacidad):
    # retorna True si puedo repartir todas las vasijas
    # en m contenedores o menos, con esa capacidad

    contenedores_usados = 1
    lleno = 0

    for vasija in vasijas:
        if lleno + vasija <= capacidad:
            lleno += vasija  ##Si entra, simplemente la agrego al contenedor.
        else:
            contenedores_usados += 1
            lleno = vasija  # Sino, agrego un contenedor y le coloco unicamente el nuevo contenido.

    return contenedores_usados <= m  # Verificar si no me pasé


def solve():
    for line in sys.stdin:
        _, m = map(int, line.split())
        vasijas = list(map(int, input().split()))

        low = max(vasijas) - 1  # invariante: la respuesta está en (low, high]
        high = sum(vasijas)

        while high > low + 1:
            mid = (low + high) // 2
            if puede_llenar(vasijas, m, mid):
                high = mid
            else:
                low = mid
        print(high)


solve()

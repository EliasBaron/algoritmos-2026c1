import sys

# qué es lo que minimizás/maximizás?
# El tamaño k de los frascos para que entren todas las leches en los contenedores.
#
# cuál es el rango lo y hi?
# low es el tamaño del frasco mas grande y hi es la suma del tamaño de todos los frascos.
#
# cómo escribís la función condicion?
# es verdadero si los contenedores_usados es menor que la cantidad de contenedores limite.


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

        low = max(vasijas)
        high = sum(vasijas)

        while low < high:
            mid = (low + high) // 2
            if puede_llenar(vasijas, m, mid):
                high = mid
            else:
                low = mid + 1
        print(low)


solve()

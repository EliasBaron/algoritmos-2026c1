## minimizing sin memoización para ver el recorrido.

import sys

INF = float("inf")
monedas = []


def coins(suma):
    # Caso base: para formar suma 0 necesito 0 monedas.
    if suma == 0:
        return 0
    # Caso base: me pasé, rama inválida.
    if suma < 0:
        return INF

    mejor = INF
    for moneda in monedas:
        mejor = min(mejor, 1 + coins(suma - moneda))

    return mejor

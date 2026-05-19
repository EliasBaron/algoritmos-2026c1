# Intevalo = (end, start)


def movie_festival(movies):
    actual_end = 0
    result = 0

    for end, start in movies:
        if actual_end <= start:
            actual_end = end
            result += 1

    return result


# En el solve debo tomar los pares, guardarlos en una lista, y ordenarlos según el fin, por eso en el par
# tiene primero el fin.
def solve():
    n = int(input())

    movies = []
    for _ in range(n):
        begin, end = map(float, input().split())
        # Guardarlos en una tupla al revés
        movies.append((end, begin))

    movies.sort()

    print(movie_festival(movies))


solve()

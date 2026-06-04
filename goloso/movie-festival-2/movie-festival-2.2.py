from bisect import bisect_right, insort


def movie_festival(movies, members):
    movies_count = 0
    for end, start in movies:
        idx = bisect_right(members, start) - 1
        if idx >= 0:
            members.pop(idx)
            insort(members, end)
            movies_count += 1
    return movies_count


def solve():
    n, m = map(int, input().split())
    movies = []
    for _ in range(n):
        start, end = map(int, input().split())
        movies.append((end, start))
    movies.sort()
    members = [0] * m
    print(movie_festival(movies, members))

    print(movie_festival(movies, members))


solve()

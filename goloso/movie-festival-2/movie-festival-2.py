import heapq


def movie_festival(movies, members):
    movies_count = 0

    for end, start in movies:
        if members[0] <= start:
            heapq.heappush(members, end)
            heapq.heappop(members)
            movies_count += 1

    return movies_count


def solve():
    n, m = map(int, input().split())

    movies = []
    for _ in range(n):
        start, end = map(int, input().split())
        movies.append((end, start))
    movies.sort()

    members = []
    for _ in range(m):
        members.append(0)

    heapq.heapify(members)

    print(movie_festival(movies, members))


solve()

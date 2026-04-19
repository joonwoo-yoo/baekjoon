import sys

sys.setrecursionlimit(10000)


def dfs(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False

    if field[y][x] == 1:
        field[y][x] = 0
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    return False


T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        field[Y][X] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                count += 1

    print(count)

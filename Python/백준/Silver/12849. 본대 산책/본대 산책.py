import sys

input = sys.stdin.readline
MOD = 1_000_000_007

D = int(input())

graph = [
    [1, 2],
    [0, 2, 3],
    [0, 1, 3, 4],
    [1, 2, 4, 5],
    [2, 3, 5, 7],
    [3, 4, 6],
    [5, 7],
    [4, 6],
]

dp = [0] * 8
dp[0] = 1

for _ in range(D):
    next_dp = [0] * 8

    for now in range(8):
        for nxt in graph[now]:
            next_dp[nxt] = (next_dp[nxt] + dp[now]) % MOD

    dp = next_dp

print(dp[0])
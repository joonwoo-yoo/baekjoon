import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

lo, hi = 0, max(trees)

while lo <= hi:
    mid = (lo + hi) // 2
    total = 0

    for t in trees:
        if t > mid:
            total += t - mid
            if total >= M:
                break

    if total >= M:
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)
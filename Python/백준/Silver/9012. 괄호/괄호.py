import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    ps = input().strip()
    count = 0
    is_vps = True

    for ch in ps:
        if ch == "(":
            count += 1
        else:
            count -= 1

        if count < 0:
            is_vps = False
            break

    if count != 0:
        is_vps = False

    print("YES" if is_vps else "NO")

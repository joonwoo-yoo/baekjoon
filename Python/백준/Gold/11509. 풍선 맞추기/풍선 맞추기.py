import sys

n = int(sys.stdin.readline())
h_list = list(map(int, sys.stdin.readline().split()))

arrows = [0] * 1000001
total_arrows = 0

for h in h_list:
    if arrows[h] > 0:
        arrows[h] -= 1
        arrows[h - 1] += 1
    else:
        total_arrows += 1
        arrows[h - 1] += 1

print(total_arrows)

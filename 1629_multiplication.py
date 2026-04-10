A, B, C = map(int, input().split())


def mod_pow(a, b):
    if b == 1:
        return a % C

    half = mod_pow(a, b // 2)

    if b % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * a) % C


print(mod_pow(A, B))

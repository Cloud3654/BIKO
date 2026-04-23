n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

def rotate(l, k):
    rl = [([0] * i) for i in range(1, n + 1)]
    if k == 1:
        for i in range(n):
            for j in range(i + 1):
                oi = (n - 1) - j
                oj = oi - (n - i) + 1
                rl[i][j] = l[oi][oj]
    else:
        for i in range(n):
            for j in range(i + 1):
                ci = (n - 1) - j
                cj = ci - (n - i) + 1
                rl[ci][cj] = l[i][j]
    return rl

def flip(l):
    rl = [([0] * i) for i in range(1, n + 1)]
    for i in range(n):
        for j in range(i + 1):
            rl[i][j] = l[i][i - j]
    return rl

def diff(a, b):
    res = 0
    for i in range(n):
        for j in range(i + 1):
            res += int(a[i][j] != b[i][j])
    return res

md = 56
for r in range(3):
    for f in range(2):
        ta = [a[i] for i in range(n)]
        if r != 0: ta = rotate(ta, r)
        if f == 1: ta = flip(ta)
        d = diff(ta, b)
        if d < md: md = d
print(md)

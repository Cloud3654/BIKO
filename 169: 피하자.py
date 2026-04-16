n = int(input())
arr = list(map(int, input().split()))
for i in range(n): arr[i] %= 2
s0, x0 = 0, 0
s1, x1 = 0, 0
for i in range(n):
    if arr[i] == 0:
        s0 += abs(x0 - i)
        x0 += 1
    else:
        s1 += abs(x1 - i)
        x1 += 1
print(min(s0, s1))

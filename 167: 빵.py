n = int(input())
m = 1001
for _ in range(n):
    a, b = map(int, input().split())
    if a <= b and b < m: m = b
if m > 1000: print(-1)
else: print(m)

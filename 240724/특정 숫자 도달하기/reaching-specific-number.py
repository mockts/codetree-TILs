x = list(map(int, input().split()))

s = 0
c = 0

for i in range(10):
    if x[i] >= 250:
        break
    s += x[i]
    c += 1

if c == 0:
    s = sum(x)
    c = len(x)

a = s / c

print(s, round(a, 1))
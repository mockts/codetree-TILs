a, b, c = map(int, input().split())

found = False
for i in range(a, b + 1):
    if i % c == 0:
        found = True
        break

if found:
    print("NO")
else:
    print("YES")
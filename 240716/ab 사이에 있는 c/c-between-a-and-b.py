a, b, c = map(int, input().split())
x = any(i % c == 0 for i in range(a, b + 1))

if x:
    print("YES")
else:
    print("NO")
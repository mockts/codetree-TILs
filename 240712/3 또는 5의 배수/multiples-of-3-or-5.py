a, b = map(int, input().split())

if a < b:
    print("1 0")
elif a > b:
    print("0 1")
else:  # a == b
    print("1 1")
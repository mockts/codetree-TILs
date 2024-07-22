a, b = map(int, input().split())

for x in [2, 4, 6, 8]:
    for i in range(b, a - 1, -1):
        if i != b:   
            print(" / ", end="")
        print(f"{i} * {x} = {i * x}", end="")
    print()
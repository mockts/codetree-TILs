def x(n):
    num = 1
    for row in range(1, n + 1):
        if row % 2 == 1:
            increment = 1
        else:
            increment = 2
        
        for col in range(n):
            print(num, end=' ')
            num += increment
        print()

n = int(input())
x(n)